from __future__ import annotations
import argparse
from pathlib import Path
import pandas as pd
import yfinance as yf
from .mapping import load_config


def trailing_12m_yield(ticker: str) -> tuple[float, str]:
    tk = yf.Ticker(ticker)
    # method 1: direct field if available
    y = None
    method = ''
    try:
        fi = getattr(tk, 'fast_info', None)
        if fi and fi.get('trailingAnnualDividendYield') is not None:
            y = float(fi.get('trailingAnnualDividendYield'))
            method = 'fast_info.trailingAnnualDividendYield'
    except Exception:
        pass

    # method 2: compute from last 12m dividends / latest adj close-ish close
    if y is None:
        try:
            div = tk.dividends
            if div is None or div.empty:
                div12 = 0.0
            else:
                cutoff = pd.Timestamp.utcnow().tz_localize(None) - pd.Timedelta(days=365)
                idx = div.index.tz_localize(None) if getattr(div.index, 'tz', None) is not None else div.index
                div12 = float(div.loc[idx >= cutoff].sum())
            h = tk.history(period='1mo', auto_adjust=False)
            if h.empty:
                raise RuntimeError(f'No price history for {ticker}')
            price = float(h['Close'].dropna().iloc[-1])
            if price <= 0:
                raise RuntimeError(f'Invalid price for {ticker}')
            y = div12 / price
            method = 'sum(last12m_dividends)/latest_close'
        except Exception as e:
            raise RuntimeError(f'Failed to compute trailing 12M yield for {ticker}: {e}')

    return max(float(y), 0.0), method


def main():
    p=argparse.ArgumentParser(); p.add_argument('--config', required=True); args=p.parse_args()
    root = Path(__file__).resolve().parents[1]
    cfg = load_config(args.config)
    out_t = root/'outputs'/'tables'; out_t.mkdir(parents=True, exist_ok=True)

    rows=[]
    for bucket, ticker in cfg['proxy_map'].items():
        y, method = trailing_12m_yield(ticker)
        rows.append({'bucket':bucket,'proxy':ticker,'trailing_12m_distribution_yield':y,'yield_method':method,'source':'yfinance'})

    ydf = pd.DataFrame(rows)
    ydf.to_csv(out_t/'asset_yield_assumptions.csv', index=False)

    summary=[]
    for pname, w in [('SAA', cfg['weights']['saa']), ('TAA', cfg['weights']['taa_static'])]:
        py = 0.0
        for b, wt in w.items():
            y = float(ydf.loc[ydf['bucket']==b, 'trailing_12m_distribution_yield'].iloc[0])
            py += wt * y
        annual = py * cfg['capital_usd']
        monthly = annual / 12
        gap = cfg['income_requirement_monthly_usd'] - monthly
        req_yield = (cfg['income_requirement_monthly_usd']*12)/cfg['capital_usd']
        summary.append({
            'portfolio': pname,
            'portfolio_income_yield': py,
            'annual_income_usd': annual,
            'monthly_income_usd': monthly,
            'income_gap_vs_25k_monthly': gap,
            'required_portfolio_yield_to_meet_target': req_yield,
            'shortfall_yield': max(req_yield-py,0),
            'source':'yfinance'
        })

    pd.DataFrame(summary).to_csv(out_t/'income_summary.csv', index=False)
    print('Income model upgraded to full portfolio cash-flow approach.')

if __name__=='__main__':
    main()
