from __future__ import annotations
import argparse
from pathlib import Path
import pandas as pd
from .mapping import load_config, build_mapping_df


def usd(x): return f"${x:,.0f}"

def expected_box(weights, bands: pd.DataFrame, portfolio_income_yield: float, cap: float, income_req: float):
    bmap=bands.set_index('bucket').to_dict('index')
    rows=[]
    for band in ['low','base','high']:
        total=sum(weights.get(k,0)*bmap[k][band] for k in bmap.keys() if k in weights)
        inc_r=portfolio_income_yield
        cg=total-inc_r
        m=inc_r*cap/12
        rows.append({'Band':band.upper(),'Total Return %':f'{total*100:.2f}%','Total Return $':usd(total*cap),'Income Return %':f'{inc_r*100:.2f}%','Income Return $':usd(inc_r*cap),'Capital Gain %':f'{cg*100:.2f}%','Capital Gain $':usd(cg*cap),'Monthly Income $':usd(m),'vs $25k Requirement':'MEET' if m>=income_req else 'SHORTFALL'})
    return pd.DataFrame(rows)

def main():
    p=argparse.ArgumentParser(); p.add_argument('--config',required=True); args=p.parse_args()
    root=Path(__file__).resolve().parents[1]
    cfg=load_config(args.config)
    out=root/'outputs'; out_t=out/'tables'

    metrics=pd.read_csv(out_t/'metrics_summary.csv')
    hist=pd.read_csv(out_t/'historical_stress_windows.csv')
    hypo=pd.read_csv(out_t/'hypothetical_scenarios.csv')
    coverage=pd.read_csv(out_t/'data_coverage_report.csv')
    tc=pd.read_csv(out_t/'transaction_cost_sensitivity.csv')
    beta=pd.read_csv(out_t/'proxy_validation_beta_stability.csv')
    bands=pd.read_csv(out_t/'bucket_return_bands.csv')
    yields=pd.read_csv(out_t/'asset_yield_assumptions.csv')
    income=pd.read_csv(out_t/'income_summary.csv')

    cap=cfg['capital_usd']; req=cfg['income_requirement_monthly_usd']
    saa=cfg['weights']['saa']; taa=cfg['weights']['taa_static']

    saa_income=float(income.loc[income['portfolio']=='SAA','portfolio_income_yield'].iloc[0])
    taa_income=float(income.loc[income['portfolio']=='TAA','portfolio_income_yield'].iloc[0])

    p1_box=expected_box(saa,bands,saa_income,cap,req)
    p2_box=expected_box(taa,bands,taa_income,cap,req)

    saa_base_row=p1_box[p1_box['Band']=='BASE'].iloc[0]
    vol=float(metrics.loc[metrics['portfolio']=='SAA','ann_vol'].iloc[0])

    taa_tbl=pd.DataFrame({'Asset':sorted(set(saa)|set(taa))})
    taa_tbl['SAA']=taa_tbl['Asset'].map(lambda x:saa.get(x,0)); taa_tbl['TAA']=taa_tbl['Asset'].map(lambda x:taa.get(x,0)); taa_tbl['Delta']=taa_tbl['TAA']-taa_tbl['SAA']
    taa_fmt=taa_tbl.assign(SAA=taa_tbl['SAA'].map(lambda x:f'{x*100:.1f}%'),TAA=taa_tbl['TAA'].map(lambda x:f'{x*100:.1f}%'),Delta=taa_tbl['Delta'].map(lambda x:f'{x*100:+.1f}%'))

    mapping_df=build_mapping_df(cfg)
    mapping_df.to_csv(out_t/'proxy_mapping.csv',index=False)

    req_yield=float(income.loc[income['portfolio']=='SAA','required_portfolio_yield_to_meet_target'].iloc[0])
    shortfall=float(income.loc[income['portfolio']=='SAA','shortfall_yield'].iloc[0])

    md=f"""## CLIENT SLIDES

# SLIDE P1 — Strategic Asset Allocation (SAA)
Title: Strategic Asset Allocation — Built Around Your Objectives

### A) Client Objectives
- Capital preservation mandate
- USD 25k/month income requirement
- Private market participation
- AI thematic exposure via diversified equity sleeves
- Liquidity buffer for flexibility

### B) Portfolio Structure
{pd.DataFrame([{'Asset/Sub-asset':k,'Weight %':v*100} for k,v in saa.items()]).to_markdown(index=False)}

### C) Client-Relevant Metrics
- Expected Return (BASE case): {saa_base_row['Total Return %']} ({saa_base_row['Total Return $']})
- Volatility: {vol}
- Portfolio Income Yield (full cash-flow model): {saa_base_row['Income Return %']} ({saa_base_row['Income Return $']})
- Income gap vs requirement: {saa_base_row['Monthly Income $']} vs $25,000/month

### D) What This Means for You
- Income is now estimated from full portfolio cash-flow capacity, not cash sleeve alone.
- Income sources include equity dividends, bond coupons, private credit distributions, and cash yield.
- The portfolio keeps strategic diversification while making income sustainability measurable.

Income Sustainability Note:
- Required portfolio yield to meet target: {req_yield*100:.2f}%.
- SAA shortfall yield: {shortfall*100:.2f}%.
- Optional overlay (no weight change shown): dedicated income sleeve via 5–10% tilt within fixed-income sleeve toward higher-distribution instruments.

# SLIDE P2 — Tactical Asset Allocation (TAA)
Title: Tactical Asset Allocation — 6–12 Month Cyclical Overlay

### A) Current Macro Backdrop
- Policy-rate plateau
- Disinflation trend
- Regional diversification opportunity

### B) Tactical Adjustments
{taa_fmt.to_markdown(index=False)}

### C) Risk Discipline Note
- Tactical bands are capped at ±2% versus SAA.
- This preserves long-term allocation discipline and strategic risk budget.

### D) Expected Impact
- BASE expected return shifts from {saa_base_row['Total Return %']} to {p2_box[p2_box['Band']=='BASE'].iloc[0]['Total Return %']}.
- The change is cyclical, not structural; core allocation remains anchored to SAA.

## APPENDIX — Quantitative Validation & Performance Decomposition
This section provides quantitative validation for the client-facing strategy.

# SLIDE A1 — Return Decomposition + Income Model
Table caption: SAA LOW/BASE/HIGH decomposition (income model upgraded)
{p1_box.to_markdown(index=False)}

Table caption: TAA LOW/BASE/HIGH decomposition (income model upgraded)
{p2_box.to_markdown(index=False)}

Table caption: Yield assumption per asset bucket (trailing 12M distribution yield)
{yields.to_markdown(index=False)}

Table caption: Backtest statistics
{metrics.to_markdown(index=False)}

Income Sustainability Note:
- Income model upgraded to full portfolio cash-flow approach.
- Portfolio income sources: equity dividends, bond coupons, private credit distributions, and cash yield.

# SLIDE A2 — Performance & Drawdown
Chart callout: outputs/charts/equity_curve.png — cumulative growth comparison.
Chart callout: outputs/charts/drawdown.png — drawdown depth/duration comparison.

Table caption: Max drawdown + recovery
{hist.groupby('portfolio',as_index=False).agg(max_drawdown=('peak_to_trough_dd','min'),avg_recovery_days=('recovery_days','mean')).to_markdown(index=False)}

# SLIDE A3 — Stress Tests
Table caption: Historical stress windows
{hist.to_markdown(index=False)}

Table caption: Hypothetical scenario impacts
{hypo.to_markdown(index=False)}

Chart callout: outputs/charts/stress_bar.png — scenario impacts sorted worst→best.

# SLIDE A4 — Distribution & Rolling Diagnostics
Chart callouts:
- outputs/charts/monthly_return_hist.png
- outputs/charts/sharpe_distribution.png
- outputs/charts/rolling_12m_return.png

# SLIDE A5 — Proxy Mapping & Model Explanation
{mapping_df.to_markdown(index=False)}

Model explanation box:
1) Download daily prices via yfinance.
2) Use adjusted close; align trading calendars.
3) Build portfolio returns with specified rebalance rules.
4) Compute return/risk metrics and drawdowns.
5) Run stress windows and hypothetical scenarios.
6) Export charts/tables and assumption notes.

Methodology robustness checks implemented: data integrity validation; transaction cost sensitivity; proxy beta stability analysis.

# SLIDE A6 — Robustness & Validation
Table caption: Data coverage report
{coverage.to_markdown(index=False)}

Table caption: Transaction cost sensitivity (0/10/25 bps)
{tc.to_markdown(index=False)}

Table caption: Proxy beta stability (rolling 12M)
{beta.to_markdown(index=False)}

Footnote: Market data sourced via yfinance; adjusted close used; see data coverage table.
"""

    (out/'slide_content.md').write_text(md, encoding='utf-8')
    (out/'research_portfolio.md').write_text('# Research Portfolio Note\n\n'+md, encoding='utf-8')
    print('Report complete')

if __name__=='__main__':
    main()
