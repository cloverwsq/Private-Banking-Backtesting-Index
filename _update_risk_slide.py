from pathlib import Path
import pandas as pd
root=Path(r'C:\Users\35882\Desktop\金融tech\openclaw\hsbc_pb_openclaw')
p=root/'outputs'/'slide_content.md'
t=p.read_text(encoding='utf-8')

# insert chart placement lines for A5-A8 if absent
repls={
'# SLIDE A5 — Backtest Metrics (Validation Only)':'# SLIDE A5 — Backtest Metrics (Validation Only)\nVisual Placement:\n- outputs/charts/equity_curve.png (Top panel)\n- outputs/charts/drawdown.png (Second panel)\n- outputs/charts/rolling_12m_return.png (Bottom-left)\n- outputs/charts/monthly_return_hist.png (Bottom-middle)\n- outputs/charts/sharpe_distribution.png (Bottom-right)\n',
'# SLIDE A6 — Stress Tests (Validation Only)':'# SLIDE A6 — Stress Tests (Validation Only)\nVisual Placement:\n- outputs/charts/stress_bar.png (Figure A6.1 — Scenario Impact Ranking)\n',
'# SLIDE A7 — Data Coverage':'# SLIDE A7 — Data Coverage\nVisual Placement:\n- No chart (table-only)\n',
'# SLIDE A8 — Transaction Cost Sensitivity':'# SLIDE A8 — Transaction Cost Sensitivity\nVisual Placement:\n- No chart (table-only)\n'
}
for k,v in repls.items():
    if k in t and 'Visual Placement' not in t[t.find(k):t.find(k)+220]:
        t=t.replace(k,v)

mc=pd.read_csv(root/'outputs'/'tables'/'monte_carlo_percentiles.csv')
var=pd.read_csv(root/'outputs'/'tables'/'var_summary.csv')
sc=pd.read_csv(root/'outputs'/'tables'/'historical_stress_windows.csv')
fund=pd.read_csv(root/'outputs'/'tables'/'monte_carlo_funding_probability.csv').iloc[0]

risk_matrix='''| Risk Category | Portfolio-Specific Manifestation | Current Control |
|:--|:--|:--|
| Equity beta drawdown | Equity sleeve can drive short-term mark-to-market losses | Diversified regional equity + alternatives |
| Credit spread widening | HY/EM debt spread shock can reduce near-term valuation | IG anchor + limited HY weight |
| Liquidity mismatch | Private markets are less liquid than public sleeves | Cash + listed liquid sleeves for near-term needs |
| Sequence risk (education horizon) | Adverse window before liability dates | Glide-path trigger (8–10y to liability) |
| Tactical drift risk | Overlay can add unintended risk | ±2% tactical bands and periodic rebalance |
'''

pct_tbl = mc.copy()
pct_tbl['terminal_wealth_usd_mn']=pct_tbl['terminal_wealth_usd_mn'].map(lambda x:f'{x:,.2f}')
var2=var.copy(); var2['VaR_1d_95']=var2['VaR_1d_95'].map(lambda x:f'{x*100:.2f}%'); var2['VaR_10d_95']=var2['VaR_10d_95'].map(lambda x:f'{x*100:.2f}%')

sc2=sc[['window','portfolio','cum_return','peak_to_trough_dd']].copy()
sc2['cum_return']=sc2['cum_return'].map(lambda x:f'{x*100:.2f}%')
sc2['peak_to_trough_dd']=sc2['peak_to_trough_dd'].map(lambda x:f'{x*100:.2f}%')

new_slide=f'''

# SLIDE A9 — Portfolio Backtesting & Downside Risk Analysis
Title: Portfolio Backtesting & Downside Risk Analysis

### Top Left — Risk Matrix (Portfolio-Specific)
{risk_matrix}

### Top Right — Monte Carlo Distribution (BASE: mu=9.6%, sigma=8.6%, horizon=13y, AUM=80m)
Visual Placement:
- outputs/charts/monte_carlo_terminal_wealth.png (Figure A9.1 — Terminal Wealth Distribution, USD mn)

Table caption: Terminal Wealth Percentiles (USD mn)
{pct_tbl.to_markdown(index=False)}

Funding probability statement:
- Education PV liability reference: USD 1.18mn.
- Probability of terminal wealth >= education PV: {fund['funding_probability']*100:.2f}%.

### Bottom Left — Historical VaR Summary (95%)
Table caption: 1-day and 10-day Historical VaR
{var2.to_markdown(index=False)}

### Bottom Right — Scenario Analysis (Historical Windows)
Table caption: COVID / rates_2022 / q4_2018 outcomes
{sc2.to_markdown(index=False)}

Narrative:
- Volatility remains controlled relative to growth objective under the strategic design.
- Education PV liability (1.18mn) is immaterial versus total AUM (80mn).
- Tactical overlay improves opportunity set without materially increasing tail-risk profile.
'''

if '# SLIDE A9 — Portfolio Backtesting & Downside Risk Analysis' not in t:
    t += new_slide

p.write_text(t,encoding='utf-8')
print('slide_content updated')
