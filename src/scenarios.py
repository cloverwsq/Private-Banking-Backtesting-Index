from __future__ import annotations
import argparse
from pathlib import Path
import pandas as pd
import numpy as np
from .mapping import load_config, EQUITY_BUCKETS, ALTERNATIVE_BUCKETS
from .charts import plot_stress_bar
from .portfolio import cumulative, drawdown

def _port_weights(cfg):
    return {
        'Current': cfg['weights']['current'],
        'SAA': cfg['weights']['saa'],
        'TAA Static': cfg['weights']['taa_static'],
        'TAA Quarterly': cfg['weights']['taa_static']
    }

def _group_shock(bucket, shocks):
    if bucket in EQUITY_BUCKETS and 'equities' in shocks: return shocks['equities']
    if bucket in ALTERNATIVE_BUCKETS and 'alternatives' in shocks: return shocks['alternatives']
    return shocks.get(bucket, 0.0)

def historical_windows(port_rets: pd.DataFrame, windows: dict):
    rows=[]
    for wname,(s,e) in windows.items():
        seg=port_rets.loc[(port_rets.index>=s)&(port_rets.index<=e)]
        if seg.empty: continue
        for p in seg.columns:
            r=seg[p]
            cum=(1+r).prod()-1
            dd=(cumulative(r)/cumulative(r).cummax()-1).min()
            eq=cumulative(r)
            rec=np.nan
            peak_idx=eq.cummax().idxmax()
            trough=eq.idxmin()
            if trough<=eq.index.max():
                post=eq.loc[trough:]
                hit=post[post>=eq.loc[:trough].max()]
                if not hit.empty: rec=(hit.index[0]-trough).days
            rows.append({'window':wname,'portfolio':p,'cum_return':cum,'peak_to_trough_dd':dd,'recovery_days':rec})
    return pd.DataFrame(rows)

def hypothetical(cfg):
    rows=[]
    ports=_port_weights(cfg)
    for sc in cfg['scenarios']:
        for pname,w in ports.items():
            impact=0.0
            for b,wt in w.items():
                impact += wt*_group_shock(b, sc['shocks'])
            rows.append({'scenario':sc['name'],'portfolio':pname,'impact_pct':impact,'impact_usd':impact*cfg['capital_usd'], 'scenario_portfolio':f"{sc['name']} | {pname}"})
    return pd.DataFrame(rows)

def main():
    p=argparse.ArgumentParser(); p.add_argument('--config',required=True); args=p.parse_args()
    root=Path(__file__).resolve().parents[1]
    cfg=load_config(args.config)
    out_t=root/'outputs'/'tables'; out_c=root/'outputs'/'charts'
    rets=pd.read_csv(out_t/'daily_portfolio_returns.csv', index_col=0, parse_dates=True)

    hist=historical_windows(rets, cfg['stress_windows'])
    hist.to_csv(out_t/'historical_stress_windows.csv', index=False)
    hypo=hypothetical(cfg)
    hypo.to_csv(out_t/'hypothetical_scenarios.csv', index=False)
    plot_stress_bar(hypo, out_c/'stress_bar.png', cfg)
    print('Scenarios complete')

if __name__=='__main__':
    main()
