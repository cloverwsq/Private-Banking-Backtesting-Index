import numpy as np, pandas as pd
from pathlib import Path
import matplotlib.pyplot as plt

root=Path(r'C:\Users\35882\Desktop\金融tech\openclaw\hsbc_pb_openclaw')
out_t=root/'outputs'/'tables'; out_c=root/'outputs'/'charts'

# Inputs from existing outputs
rets=pd.read_csv(out_t/'daily_portfolio_returns.csv', index_col=0, parse_dates=True)
stress=pd.read_csv(out_t/'historical_stress_windows.csv')
metrics=pd.read_csv(out_t/'metrics_summary.csv')

# Monte Carlo settings
mu=0.096
sigma=0.086
horizon=13
aum=80_000_000
n=20000
rng=np.random.default_rng(20260301)
# lognormal one-step over horizon
z=rng.standard_normal(n)
term = aum*np.exp((mu-0.5*sigma**2)*horizon + sigma*np.sqrt(horizon)*z)
term_mn = term/1_000_000

# percentiles
pct=[1,5,10,25,50,75,90,95,99]
vals=np.percentile(term_mn,pct)
mc_tbl=pd.DataFrame({'percentile':[f'p{p}' for p in pct],'terminal_wealth_usd_mn':vals})
mc_tbl.to_csv(out_t/'monte_carlo_percentiles.csv', index=False)

# probability funding education PV
pv=1_182_870
prob=float((term>=pv).mean())
pd.DataFrame([{'mu':mu,'sigma':sigma,'horizon_years':horizon,'aum':aum,'education_pv':pv,'funding_probability':prob}]).to_csv(out_t/'monte_carlo_funding_probability.csv',index=False)

# chart
fig,ax=plt.subplots(figsize=(8,4.5))
ax.hist(term_mn,bins=80,alpha=0.85)
ax.axvline(pv/1_000_000,color='red',linestyle='--',label='Education PV = 1.18mn')
ax.set_title('Monte Carlo Terminal Wealth Distribution (USD mn)')
ax.set_xlabel('Terminal Wealth (USD mn)')
ax.set_ylabel('Frequency')
ax.legend()
fig.tight_layout(); fig.savefig(out_c/'monte_carlo_terminal_wealth.png',dpi=250); plt.close(fig)

# VaR historical from returns
rows=[]
for p in ['SAA','TAA Static','TAA Quarterly','Current']:
    if p not in rets.columns: continue
    r=rets[p].dropna()
    var1=-np.percentile(r,5)
    var10=-np.percentile(r.rolling(10).sum().dropna(),5)
    rows.append({'portfolio':p,'VaR_1d_95':var1,'VaR_10d_95':var10})
var_tbl=pd.DataFrame(rows)
var_tbl.to_csv(out_t/'var_summary.csv',index=False)

# Scenario summary pivot
sc=stress.pivot(index='window',columns='portfolio',values='cum_return').reset_index()
sc.to_csv(out_t/'scenario_summary_pivot.csv',index=False)

print('generated monte carlo, var, scenario summary')
