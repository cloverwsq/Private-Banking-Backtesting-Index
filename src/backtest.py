from __future__ import annotations
import argparse
from pathlib import Path
import numpy as np
import pandas as pd
import yfinance as yf
from .mapping import load_config
from .portfolio import portfolio_returns, drawdown
from .charts import plot_equity_curve, plot_drawdown, plot_rolling_12m, plot_monthly_hist, plot_sharpe_distribution


def annualized_return(r): return (1+r).prod()**(252/max(len(r),1))-1 if len(r)>0 else np.nan
def annualized_vol(r): return r.std()*np.sqrt(252)
def sharpe(r, rf=0.0):
    ex=r-rf/252; s=ex.std(); return np.nan if s==0 else ex.mean()/s*np.sqrt(252)
def sortino(r, rf=0.0):
    ex=r-rf/252; s=ex[ex<0].std(); return np.nan if s==0 else ex.mean()/s*np.sqrt(252)
def calmar(r):
    dd=drawdown(r).min(); return np.nan if dd==0 else annualized_return(r)/abs(dd)

def download_adj_close_strict(tickers, start, end=None):
    raw = yf.download(tickers=tickers, start=start, end=end, auto_adjust=False, actions=True, progress=False)
    if raw is None or raw.empty:
        raise RuntimeError('LIVE DATA MODE: yfinance download returned empty dataset')
    cols = raw.columns.get_level_values(0)
    if 'Adj Close' not in cols:
        raise RuntimeError('LIVE DATA MODE: Adj Close not present in yfinance payload')
    adj = raw['Adj Close']
    if isinstance(adj, pd.Series):
        adj = adj.to_frame()
    adj = adj.sort_index()
    if adj.shape[0] < 252:
        raise RuntimeError(f'LIVE DATA MODE: insufficient history rows={adj.shape[0]}')
    return adj

def build_coverage_report(adj: pd.DataFrame):
    cal = pd.DataFrame(index=pd.bdate_range(adj.index.min(), adj.index.max()))
    aligned = cal.join(adj, how='left')
    rows=[]
    for t in aligned.columns:
        s = aligned[t]
        cov = 1 - s.isna().mean()
        rows.append({
            'ticker': t,
            'start_date': str(s.first_valid_index().date()) if s.first_valid_index() is not None else 'NA',
            'end_date': str(s.last_valid_index().date()) if s.last_valid_index() is not None else 'NA',
            'coverage_pct': cov*100,
            'missing_days_pct': (1-cov)*100,
            'source': 'yfinance'
        })
    rep = pd.DataFrame(rows)
    bad = rep.loc[rep['coverage_pct'] < 95, 'ticker'].tolist()
    if bad:
        raise RuntimeError(f'LIVE DATA MODE: coverage <95% for tickers={bad}')
    return aligned.ffill().dropna(), rep

def summary_metrics(portfolios, rf_annual):
    rows=[]; saa=portfolios['SAA']
    for n,r in portfolios.items():
        m=r.resample('ME').apply(lambda x:(1+x).prod()-1)
        rows.append({'portfolio':n,'cagr':annualized_return(r),'ann_vol':annualized_vol(r),'sharpe_rf0':sharpe(r,0.0),'sharpe_rf_cash':sharpe(r,rf_annual),'sortino':sortino(r,rf_annual),'max_drawdown':drawdown(r).min(),'calmar':calmar(r),'worst_month':m.min(),'best_month':m.max(),'%positive_months':(m>0).mean(),'tracking_error_vs_saa':((r-saa).std()*np.sqrt(252) if n!='SAA' else 0.0)})
    return pd.DataFrame(rows)

def build_bucket_bands(bucket_returns: pd.DataFrame):
    rows=[]
    for c in bucket_returns.columns:
        mu = bucket_returns[c].mean()*252
        vol = bucket_returns[c].std()*np.sqrt(252)
        rows.append({'bucket':c,'low':mu-vol,'base':mu,'high':mu+vol})
    return pd.DataFrame(rows)

def main():
    p=argparse.ArgumentParser(); p.add_argument('--config',required=True); args=p.parse_args()
    root=Path(__file__).resolve().parents[1]; cfg=load_config(args.config)
    out_t=root/'outputs'/'tables'; out_c=root/'outputs'/'charts'; out_t.mkdir(parents=True,exist_ok=True); out_c.mkdir(parents=True,exist_ok=True)

    tickers=sorted(set(cfg['proxy_map'].values()))
    adj=download_adj_close_strict(tickers,cfg['start_date'],cfg.get('end_date'))
    px,coverage=build_coverage_report(adj)
    coverage.to_csv(out_t/'data_coverage_report.csv', index=False)

    rets=px.pct_change().dropna()
    bucket=pd.DataFrame({b:rets[t] for b,t in cfg['proxy_map'].items()}, index=rets.index).dropna()
    bucket.to_csv(out_t/'bucket_daily_returns.csv')

    bands=build_bucket_bands(bucket)
    bands.to_csv(out_t/'bucket_return_bands.csv', index=False)

    cash_proxy=cfg['proxy_map']['cash']
    cash_ann=annualized_return(rets[cash_proxy])
    pd.DataFrame([{'cash_proxy':cash_proxy,'cash_annual_return':cash_ann,'method':'annualized return from yfinance adjusted close'}]).to_csv(out_t/'cash_return_methodology.csv',index=False)

    w=cfg['weights']; rb=cfg['rebalancing']; tc=cfg.get('transaction_cost_bps',0)
    ports={'Current':portfolio_returns(bucket,w['current'],rb['current'],tc),'SAA':portfolio_returns(bucket,w['saa'],rb['saa'],tc),'TAA Static':portfolio_returns(bucket,w['taa_static'],rb['taa_static'],tc),'TAA Quarterly':portfolio_returns(bucket,w['taa_static'],rb['taa_quarterly'],tc)}
    df=pd.DataFrame(ports).dropna(); df.to_csv(out_t/'daily_portfolio_returns.csv')

    metrics=summary_metrics({c:df[c] for c in df.columns},cash_ann); metrics.to_csv(out_t/'metrics_summary.csv',index=False)
    monthly=(1+df).resample('ME').prod()-1; monthly.to_csv(out_t/'monthly_returns.csv')

    plot_equity_curve(df,out_c/'equity_curve.png',cfg); plot_drawdown(df,out_c/'drawdown.png',cfg); plot_rolling_12m(monthly,out_c/'rolling_12m_return.png',cfg); plot_monthly_hist(monthly,out_c/'monthly_return_hist.png',cfg); plot_sharpe_distribution(df,out_c/'sharpe_distribution.png',cfg)
    print('Backtest complete (LIVE DATA MODE)')

if __name__=='__main__': main()
