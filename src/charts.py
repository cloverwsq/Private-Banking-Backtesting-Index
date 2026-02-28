from __future__ import annotations
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from .portfolio import cumulative, drawdown

def _style(cfg):
    plt.style.use(cfg.get('chart',{}).get('style','seaborn-v0_8-whitegrid'))

def _save(fig, path, cfg):
    fig.tight_layout(); fig.savefig(path, dpi=cfg.get('chart',{}).get('dpi',250)); plt.close(fig)

def plot_equity_curve(df: pd.DataFrame, out, cfg):
    _style(cfg); fig,ax=plt.subplots(figsize=(10,5))
    for c in df.columns: ax.plot(cumulative(df[c]), label=c, lw=1.7)
    ax.set_title('Cumulative Growth of $1'); ax.set_ylabel('Growth'); ax.legend()
    _save(fig,out,cfg)

def plot_drawdown(df, out, cfg):
    _style(cfg); fig,ax=plt.subplots(figsize=(10,5))
    for c in df.columns: ax.plot(drawdown(df[c]), label=c, lw=1.5)
    ax.set_title('Drawdown Series'); ax.set_ylabel('Drawdown'); ax.legend()
    _save(fig,out,cfg)

def plot_rolling_12m(monthly, out, cfg):
    _style(cfg); fig,ax=plt.subplots(figsize=(10,5))
    roll=(1+monthly).rolling(12).apply(np.prod,raw=True)-1
    for c in monthly.columns: ax.plot(roll[c], label=c, lw=1.5)
    ax.set_title('Rolling 12M Return'); ax.set_ylabel('Return'); ax.legend()
    _save(fig,out,cfg)

def plot_monthly_hist(monthly, out, cfg):
    _style(cfg); fig,axs=plt.subplots(2,2,figsize=(10,7)); axs=axs.flatten()
    for i,c in enumerate(monthly.columns): axs[i].hist(monthly[c].dropna(), bins=30, alpha=0.8); axs[i].set_title(c)
    _save(fig,out,cfg)

def plot_sharpe_distribution(df, out, cfg):
    _style(cfg); fig,ax=plt.subplots(figsize=(10,5))
    w=cfg.get('rolling_window_days',252)
    for c in df.columns:
        rs=(df[c].rolling(w).mean()/df[c].rolling(w).std()*np.sqrt(252)).dropna()
        ax.hist(rs, bins=30, alpha=0.45, label=c)
    ax.set_title('Rolling Sharpe Distribution'); ax.legend()
    _save(fig,out,cfg)

def plot_stress_bar(stress_df, out, cfg):
    _style(cfg); fig,ax=plt.subplots(figsize=(10,6))
    s=stress_df.sort_values('impact_pct')
    ax.barh(s['scenario_portfolio'], s['impact_pct']*100)
    ax.set_title('Scenario Impacts (worst to best)'); ax.set_xlabel('Impact (%)')
    _save(fig,out,cfg)
