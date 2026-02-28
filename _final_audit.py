import pandas as pd, yaml
from pathlib import Path
root=Path(r'C:\Users\35882\Desktop\金融tech\openclaw\hsbc_pb_openclaw')
cfg=yaml.safe_load(open(root/'config'/'config.yaml',encoding='utf-8'))
cap=cfg['capital_usd']
issues=[]
for name,w in cfg['weights'].items():
    s=sum(w.values())
    if abs(s-1)>1e-9:
        issues.append(f'weights {name} sum {s}')
m=pd.read_csv(root/'outputs'/'tables'/'metrics_summary.csv')
for p in ['Current','SAA','TAA Static','TAA Quarterly']:
    if p not in set(m['portfolio']):
        issues.append(f'metrics missing {p}')
inc=pd.read_csv(root/'outputs'/'tables'/'income_summary.csv')
for _,r in inc.iterrows():
    calc_annual=r['portfolio_income_yield']*cap
    calc_month=calc_annual/12
    if abs(calc_annual-r['annual_income_usd'])>1:
        issues.append(f"income annual mismatch {r['portfolio']}")
    if abs(calc_month-r['monthly_income_usd'])>1:
        issues.append(f"income monthly mismatch {r['portfolio']}")
req_y=300000/cap
cov=pd.read_csv(root/'outputs'/'tables'/'data_coverage_report.csv')
if (cov['coverage_pct']<95).any():
    issues.append('coverage below 95')
if not (cov['source']=='yfinance').all():
    issues.append('non-yfinance source in coverage')
hypo=pd.read_csv(root/'outputs'/'tables'/'hypothetical_scenarios.csv')
if len(hypo)!=32:
    issues.append(f'hypo rows {len(hypo)} != 32')
print('REQ_YIELD',round(req_y,6))
print('SAA monthly',round(float(inc[inc.portfolio=='SAA']['monthly_income_usd'].iloc[0]),2))
print('TAA monthly',round(float(inc[inc.portfolio=='TAA']['monthly_income_usd'].iloc[0]),2))
print('ISSUES', 'NONE' if not issues else '; '.join(issues))
