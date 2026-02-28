from __future__ import annotations
import argparse
from pathlib import Path
import numpy as np
import pandas as pd
from .mapping import load_config, EQUITY_BUCKETS
from .portfolio import portfolio_returns, drawdown


def annualized_return(r): return (1+r).prod()**(252/max(len(r),1))-1 if len(r)>0 else np.nan
def sharpe(r, rf=0.0):
    ex=r-rf/252; s=ex.std(); return np.nan if s==0 else ex.mean()/s*np.sqrt(252)

def rolling_beta(y, x, window=252):
    return y.rolling(window).cov(x) / x.rolling(window).var()

def main():
    p=argparse.ArgumentParser(); p.add_argument('--config', required=True); args=p.parse_args()
    root=Path(__file__).resolve().parents[1]
    cfg=load_config(args.config)
    out_t=root/'outputs'/'tables'; out_t.mkdir(parents=True,exist_ok=True)

    coverage=pd.read_csv(out_t/'data_coverage_report.csv')
    if (coverage['source']!='yfinance').any():
        raise RuntimeError('LIVE DATA MODE: non-yfinance source detected in data coverage report')
    if (coverage['coverage_pct']<95).any():
        raise RuntimeError('LIVE DATA MODE: coverage threshold failed')

    bucket=pd.read_csv(out_t/'bucket_daily_returns.csv', index_col=0, parse_dates=True)

    cash_ann=float(pd.read_csv(out_t/'cash_return_methodology.csv').loc[0,'cash_annual_return'])

    # transaction cost sensitivity
    rows=[]
    port_defs={
        'Current': (cfg['weights']['current'], cfg['rebalancing']['current']),
        'SAA': (cfg['weights']['saa'], cfg['rebalancing']['saa']),
        'TAA Static': (cfg['weights']['taa_static'], cfg['rebalancing']['taa_static']),
        'TAA Quarterly': (cfg['weights']['taa_static'], cfg['rebalancing']['taa_quarterly'])
    }
    for bps in [0,10,25]:
        for n,(w,rb) in port_defs.items():
            r=portfolio_returns(bucket,w,rb,bps)
            rows.append({'tc_bps':bps,'portfolio':n,'cagr':annualized_return(r),'sharpe_rf_cash':sharpe(r,cash_ann),'max_drawdown':drawdown(r).min()})
    pd.DataFrame(rows).to_csv(out_t/'transaction_cost_sensitivity.csv', index=False)

    # beta stability
    spy = bucket['us_equity']
    val=[]
    for b in EQUITY_BUCKETS:
        beta=rolling_beta(bucket[b], spy, 252).dropna()
        val.append({'bucket':b,'proxy':cfg['proxy_map'][b],'metric':'rolling_12m_beta_vs_spy','beta_mean':beta.mean(),'beta_std':beta.std(),'beta_min':beta.min(),'beta_max':beta.max()})

    if 'global_ig' in bucket.columns and 'us_equity' in bucket.columns:
        b_ig=rolling_beta(bucket['global_ig'], bucket['us_equity'], 252).dropna()
        val.append({'bucket':'global_ig','proxy':cfg['proxy_map']['global_ig'],'metric':'rolling_12m_beta_vs_us_equity_proxy','beta_mean':b_ig.mean(),'beta_std':b_ig.std(),'beta_min':b_ig.min(),'beta_max':b_ig.max()})

    pd.DataFrame(val).to_csv(out_t/'proxy_validation_beta_stability.csv', index=False)
    (out_t/'robustness_interpretation.txt').write_text('Methodology robustness checks implemented: data integrity validation; transaction cost sensitivity; proxy beta stability analysis', encoding='utf-8')
    print('Robustness validation complete (LIVE DATA MODE)')

if __name__=='__main__':
    main()
