PRF (Ultra-Production) — HSBC PB Case Challenge 2026 (Qualifier) — Portfolio Slides + Institutional Backtesting Pack



ROLE

You are OpenClaw acting as:

\- Multi-asset portfolio strategist (PB / CIO style)

\- Quant researcher (backtesting + stress testing)

\- Backtest/report engineer (tables/charts + slide-ready writing)



IMPORTANT OUTPUT RULE

I (the user) will build the slides. You MUST output slide-by-slide CONTENT only (no PPT/PPTX generation).

For each slide, output:

\- Title

\- 1-sentence Key message

\- Paste-ready tables (markdown + CSV-friendly)

\- Chart callouts (filename + 1–2 line caption)

\- Footnotes (assumptions + traceability)



OBJECTIVE

Build the “Portfolio” section for HSBC PB Case Challenge 2026 (Qualifier):

1\) Research note (auditable, case-grounded, transparent assumptions)

2\) Reproducible backtesting code + outputs (institutional charts/tables)

3\) Two core slides: SAA + TAA with expected cash return + capital gain return

4\) Appendix “Backtesting \& Risk Pack” (4–6 slide contents) with professional visuals:

&nbsp;  - equity curve comparison

&nbsp;  - drawdown series + max drawdown table

&nbsp;  - rolling 12M return

&nbsp;  - return distribution + Sharpe distribution across rolling windows

&nbsp;  - historical stress windows + hypothetical scenario grid

&nbsp;  - stress bar chart

&nbsp;  - proxy mapping + model explanation box

You do NOT have benchmark screenshots; you must still deliver “Natixis-like” clean formatting.



INPUT FILES (LOCAL PATHS)

\- Case pack PDF: /mnt/data/HSBC PB Case Challenge 2026 Qualifier Round Case.pdf

\- Preparation doc: /mnt/data/Private Banking Case Challenge Preparation.docx

\- Team deck template: /mnt/data/HSBC PB.pptx

\- Reference example deck: /mnt/data/Singapore\_Axel Cap\_Presentation\_Final Round.pdf



HARD CONSTRAINTS (NON-NEGOTIABLE)

A) Case metrics only:

\- For fund-level metrics (annualized return, annualized vol, AR, correlations, etc.), use ONLY the case Appendix I \& II.

\- Never claim dividend/distribution yield is from the case unless explicitly stated (assume it is NOT provided).

B) Cash return estimation:

\- Provide a transparent method + LOW/BASE/HIGH sensitivity band.

\- Label assumptions clearly in footnotes.

C) Backtesting uses public proxies:

\- Must map each bucket to a liquid proxy (ETF/index) with rationale + limitations.

\- Must not oversell precision. Include “proxy limitations” footnote on relevant slides.

D) Reproducibility:

\- One command generates ALL outputs (tables + charts) end-to-end.

E) Slide outputs:

\- Provide content for each slide listed under DELIVERABLES. No missing sections.



CLIENT FACTS (MUST MATCH CASE)

\- Capital to deploy: USD 80m

\- Income requirement: ≥ USD 25k/month (= USD 300k/year)

\- Current holdings proxy: 78% equities (US-heavy), 2% fixed income, 20% cash

\- Need to propose SAA + TAA; include expected cash return and expected capital gain return.



PORTFOLIO TARGETS (WEIGHTS MUST SUM 100%)

SAA (PB base case):

\- Equities 45% (US 15, Europe 10, Japan 10, Asia ex-Japan 10)

\- Fixed Income 30% (Global IG 15, Global HY 5, EM Debt 10)

\- Alternatives 20% (Private Markets/RE 12, Hedge Funds 8)

\- Cash 5%



TAA (PB realistic tilts, 6–12M):

\- Equities 47% (US 13, Europe 10, Japan 12, Asia ex-Japan 12)

\- Fixed Income 28% (IG 17, HY 3, EM 8)

\- Alternatives 22% (Private Markets 14, Hedge Funds 8)

\- Cash 3%

Include Δ column vs SAA and 3 macro bullets.



FUND REPRESENTATIVES (CASE APPENDIX ONLY; cite exact appendix rows)

Choose bucket representatives from Appendix I/II and cite:

\- US Equity: JPMorgan America Equity Fund (LU0210528500)

\- Europe Equity: HSBC GIF Euroland Value Equity (LU1193295406)

\- Japan Equity: Pictet Japanese Equity Opportunities (LU0936264273)

\- Asia ex-Japan Equity: Schroder Asian Equity Yield (LU0188438112) OR HSBC Asia ex Japan Equity High Dividend (LU0197773160)

\- Global IG: HSBC Global IG Securitised Credit (LU1728044204) \[key: low vol + AR 80%]

\- Global HY: Schroder Global High Yield (LU0418832605) or closest match in appendix

\- EM Debt: choose best match available in appendix; justify in 1 sentence

\- Private Credit / Private Markets: use Appendix II (whichever aligns) and cite

\- Hedge Fund: Global Multi-Strategy Multi-PM (Appendix II); optional global macro if present

\- Cash: conservative cash proxy (assumption)



EXPECTED CASH RETURN vs CAPITAL GAIN (MANDATORY)

Because case does not give yields explicitly:

\- Implement cash return estimation with 3-case sensitivity: LOW / BASE / HIGH.

\- Define a conservative proxy rule (e.g., cash proxy annual rate band).

Outputs required for SAA and TAA:

\- cash return % and $ (LOW/BASE/HIGH)

\- total expected return % and $

\- capital gain % and $ (= total expected return − cash return), with LOW/BASE/HIGH

\- monthly income implied vs USD 25k required

Must show whether income requirement is met under LOW case; if not, propose small adjustment and explain.



BACKTESTING — “INSTITUTIONAL” (NO BENCHMARK IMAGES PROVIDED)

You must create clean, consistent, publication-quality outputs:

\- consistent typography, labels, legend, footnote style

\- 200–300 dpi PNG exports

\- use matplotlib only; avoid overly colorful visuals; use readable layout

\- where multiple series exist, ensure clarity with line styles and markers



A) Data \& Proxy Mapping (public time series; use yfinance)

Map each bucket to a liquid proxy (ETF/index) and document:

\- US Equity: SPY (or VTI)

\- Europe Equity: VGK (or FEZ)

\- Japan Equity: EWJ

\- Asia ex-Japan: AIA (or broad Asia ex-Japan ETF available)

\- Global IG: AGG or BND (or IGLB)

\- Global HY: HYG or JNK

\- EM Debt: EMB (hard) or EMLC (local) — choose one and justify

\- Private Markets/Private Credit: BIZD preferred; if unavailable, approximate using HY with volatility scaling + smoothing; disclose

\- Hedge Fund: use conservative alt proxy such as BTAL or a blended proxy (e.g., 60% AGG + 40% SPY) with volatility targeting; disclose

\- Cash: BIL or 0% baseline (but document which)



B) Portfolios to backtest (must produce all)

1\) Current client mix proxy: 78% Equity (US-heavy proxy), 2% HY, 20% Cash

2\) Proposed SAA (monthly rebalance)

3\) Proposed TAA static (no rebalance or monthly—define clearly)

4\) Proposed TAA quarterly rebalanced

Optional: Risk parity variant only if time allows.



C) Rebalancing \& Costs

\- SAA: monthly rebalance

\- TAA: quarterly rebalance for the “reb” variant

\- Transaction costs: sensitivity 0 bps vs 10 bps per rebalance (apply to turnover)

Report gross and net-of-cost if implemented.



D) Metrics table (single table output)

For each portfolio:

\- CAGR, annualized vol

\- Sharpe (rf=0 and rf=cash-proxy)

\- Sortino

\- Max drawdown

\- Calmar

\- Worst month, best month

\- % positive months

\- Tracking error vs SAA (for TAA variants)



E) Stress tests \& scenario analysis (institutional pack)

E1 Historical stress windows (slice analysis):

\- COVID shock: 2020-02-15 to 2020-04-30 (nearest trading dates)

\- 2022 rate shock: 2022-01-01 to 2022-10-31

\- 2018 Q4 selloff: 2018-10-01 to 2018-12-31 (if data available)

For each window and portfolio output:

\- cumulative return

\- peak-to-trough drawdown

\- recovery time (days to regain previous peak, if recovered)



E2 Hypothetical scenario grid (linear approximation)

Create scenario table with bucket shocks:

\- Equity rally +10%, +20%

\- Equity selloff −10%, −20%, −30%

\- Rates up shock: IG −5% with equities −10%

\- Credit spread shock: HY −10% with equities −15%

\- Perfect storm: equities −30%, HY −15%, IG −5%, EM −12%, alternatives −8%

Rule: portfolio impact = sum(bucket weight × bucket shock). For alternatives, disclose assumptions.



E3 Stress test bar chart

\- Horizontal bars sorted worst→best

\- Show impacts for each portfolio (separate panels or separate charts)

\- Must be slide-ready



F) Model explanation box (slide-ready, 6 steps)

1\) Download daily prices (proxies)

2\) Compute daily returns; align calendars; handle missing values

3\) Construct portfolio returns with rebalancing rules

4\) Compute performance/risk metrics \& drawdowns

5\) Run stress windows + hypothetical scenarios

6\) Save charts/tables; document assumptions



OUTPUTS (FILES \& STRUCTURE) — MUST CREATE

Repo structure:

\- /config/config.yaml

\- /data/raw

\- /data/processed

\- /src

&nbsp; - extract\_case.py (parse Appendix I/II tables into csv)

&nbsp; - mapping.py (bucket -> proxy mapping)

&nbsp; - portfolio.py (weights + rebalancing)

&nbsp; - backtest.py (performance + metrics)

&nbsp; - scenarios.py (historical \& hypothetical)

&nbsp; - charts.py (matplotlib charts; consistent style)

&nbsp; - report.py (export tables)

\- /outputs

&nbsp; - tables/\*.csv

&nbsp; - charts/\*.png

&nbsp; - research\_portfolio.md

&nbsp; - README.md (exact run steps)



RUN COMMANDS (ONE-SHOT)

Provide exact commands to run end-to-end:

\- pip install -r requirements.txt

\- python -m src.extract\_case --case "/mnt/data/HSBC PB Case Challenge 2026 Qualifier Round Case.pdf"

\- python -m src.backtest --config config/config.yaml

\- python -m src.scenarios --config config/config.yaml

\- python -m src.report --config config/config.yaml



CHART SPECS (MUST FOLLOW)

All charts:

\- export PNG at 200–300 dpi

\- clear axes labels + legend

\- consistent layout and fonts

Required charts (filenames must match):

1\) outputs/charts/equity\_curve.png — cumulative growth of $1 (all portfolios)

2\) outputs/charts/drawdown.png — drawdown series (all portfolios)

3\) outputs/charts/rolling\_12m\_return.png — rolling 12M return

4\) outputs/charts/monthly\_return\_hist.png — histogram of monthly returns

5\) outputs/charts/sharpe\_distribution.png — Sharpe distribution across rolling windows

6\) outputs/charts/stress\_bar.png — scenario impacts horizontal bars



DELIVERABLES — SLIDE-BY-SLIDE CONTENT (MANDATORY)

You MUST output the following in order, with paste-ready content:



SLIDE P1 — Strategic Asset Allocation (SAA)

\- Title

\- Key message (1 sentence)

\- SAA table (Asset | Sub-asset | Weight %)

\- Expected return box:

&nbsp; - Total expected return % and $ (annual)

&nbsp; - Cash return % and $ (LOW/BASE/HIGH)

&nbsp; - Capital gain % and $ (LOW/BASE/HIGH)

&nbsp; - Monthly income vs $25k requirement (LOW/BASE/HIGH)

\- Footnotes (cash method + appendix citations)



SLIDE P2 — Tactical Asset Allocation (TAA)

\- Title

\- Key message

\- Table: Asset | SAA | TAA | Δ

\- 3 macro bullets (CIO tone; 6–12M horizon)

\- Note on rebalancing frequency + risk control

\- Footnotes



SLIDE A1 — Backtest Summary (Appendix)

\- Title

\- Paste-ready metrics table (Current vs SAA vs TAA variants)

\- 3 bullet interpretation



SLIDE A2 — Performance \& Drawdown (Appendix)

\- Title

\- Chart callouts: equity\_curve.png, drawdown.png

\- Captions: cycle resilience + drawdown control

\- Small table: Max drawdown + recovery time (if available)



SLIDE A3 — Stress Tests (Appendix)

\- Title

\- Historical stress windows table

\- Hypothetical scenario table (Scenario | Shocks | P\&L % | P\&L $ for each portfolio)

\- Chart callout: stress\_bar.png

\- 2–3 bullets interpreting worst-case protection



SLIDE A4 — Distribution \& Sharpe (Appendix)

\- Title

\- Chart callouts: monthly\_return\_hist.png, sharpe\_distribution.png, rolling\_12m\_return.png

\- Captions: stability, left-tail control, risk-adjusted outcomes



SLIDE A5 — Proxy Mapping \& Model Explanation (Appendix)

\- Title

\- Proxy mapping table (Bucket | Proxy | Rationale | Limitation)

\- Model explanation box (6 steps)

\- Limitations footnote (proxy + yfinance + costs)



QUALITY CHECKS (MUST PASS)

\- All weight tables sum to 100.00% exactly.

\- Scenario impacts consistent with weights × shocks.

\- Every number is either:

&nbsp; (i) traced to Appendix I/II (cite table/row), OR

&nbsp; (ii) explicitly labeled assumption with sensitivity band.

\- Outputs reproducible via run commands.

\- Output must be readable and slide-ready.



NO FOLLOW-UP QUESTIONS

Proceed with best-effort assumptions, document them, and deliver all deliverables.

