from __future__ import annotations
import numpy as np
import pandas as pd

FREQ_MAP = {'monthly': 'M', 'quarterly': 'Q'}

def normalize_weights(w: dict) -> dict:
    s = sum(w.values())
    return {k: v/s for k,v in w.items()}

def portfolio_returns(asset_returns: pd.DataFrame, weights: dict, rebalance='monthly', cost_bps=0.0) -> pd.Series:
    w = pd.Series(normalize_weights(weights)).reindex(asset_returns.columns).fillna(0.0)
    if rebalance == 'none':
        return (asset_returns * w).sum(axis=1)
    freq = FREQ_MAP.get(rebalance, 'M')
    returns = []
    curr_w = w.copy()
    for dt, row in asset_returns.iterrows():
        r = float((row * curr_w).sum())
        returns.append(r)
        curr_w = curr_w * (1 + row)
        if curr_w.sum() != 0:
            curr_w = curr_w / curr_w.sum()
        if (freq == 'M' and dt.is_month_end) or (freq == 'Q' and dt.is_quarter_end):
            target = w
            turnover = float((target - curr_w).abs().sum())
            cost = turnover * (cost_bps/10000.0)
            returns[-1] -= cost
            curr_w = target.copy()
    return pd.Series(returns, index=asset_returns.index)

def cumulative(series: pd.Series) -> pd.Series:
    return (1 + series).cumprod()

def drawdown(series: pd.Series) -> pd.Series:
    eq = cumulative(series)
    return eq/eq.cummax() - 1
