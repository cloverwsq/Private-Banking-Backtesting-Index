## CLIENT SLIDES

# SLIDE P1 — Strategic Asset Allocation (SAA)
Title: Strategic Asset Allocation — Built Around Your Objectives

### A) Client Objectives
- Capital preservation mandate
- USD 25k/month income requirement
- Private market participation
- AI thematic exposure via diversified equity sleeves
- Liquidity buffer for flexibility

### B) Portfolio Structure
| Asset/Sub-asset      |   Weight % |
|:---------------------|-----------:|
| us_equity            |         15 |
| europe_equity        |         10 |
| japan_equity         |         10 |
| asia_ex_japan_equity |         10 |
| global_ig            |         15 |
| global_hy            |          5 |
| em_debt              |         10 |
| private_markets      |         12 |
| hedge_funds          |          8 |
| cash                 |          5 |

### C) Client-Relevant Metrics (BASE only, case-compliant source)
- Expected Return (BASE case): **Sourced from Case Appendix I/II (see A1 Case-Sourced Decomposition)**
- Volatility: **0.0969827686196899** (proxy backtest validation; see A1/A6)
- Portfolio Income Yield (full cash-flow model): **4.37% ($3,492,317)**
- Monthly income vs requirement: **$291,026 vs $25,000/month**

### D) What This Means for You
- Strategic allocation is set by client objectives and strategic risk budget.
- Expected return assumptions for investment decisioning are case-sourced (Appendix I/II).
- Historical behavior is validated separately using proxy backtests.

### Visual Placement
- Primary visual (center): Allocation structure table.
- Optional small visual: asset-allocation bar chart from table weights.
- No heavy backtest/stress charts on this page.

### Footnotes / Appendix Cross-References
- Case-sourced expected return decomposition: Appendix A1.
- Risk statistics and stress validation: Appendix A1–A4.
- Income decomposition methodology: Appendix A1.
- Data integrity and robustness checks: Appendix A6.

---

# SLIDE P2 — Tactical Asset Allocation (TAA)
Title: Tactical Asset Allocation — 6–12 Month Cyclical Overlay

### A) Current Macro Backdrop
- Policy-rate plateau
- Disinflation trend
- Regional diversification opportunity

### B) Tactical Adjustments (Delta vs SAA)
| Asset                | SAA   | TAA   | Delta   |
|:---------------------|:------|:------|:--------|
| asia_ex_japan_equity | 10.0% | 12.0% | +2.0%   |
| cash                 | 5.0%  | 3.0%  | -2.0%   |
| em_debt              | 10.0% | 8.0%  | -2.0%   |
| europe_equity        | 10.0% | 10.0% | +0.0%   |
| global_hy            | 5.0%  | 3.0%  | -2.0%   |
| global_ig            | 15.0% | 17.0% | +2.0%   |
| hedge_funds          | 8.0%  | 8.0%  | +0.0%   |
| japan_equity         | 10.0% | 12.0% | +2.0%   |
| private_markets      | 12.0% | 14.0% | +2.0%   |
| us_equity            | 15.0% | 13.0% | -2.0%   |

### C) Risk Discipline Note
- Tactical bands are capped at ±2% versus SAA.
- This preserves long-term allocation discipline and strategic risk budget.

### D) Expected Impact (BASE only, case-compliant source)
- BASE expected return shift is derived from Case Appendix I/II decomposition (see Appendix A1).
- LOW/HIGH tactical decomposition is moved entirely to Appendix A1.

### Visual Placement
- Primary visual: SAA vs TAA delta bar chart.
- No stress charts on this slide.

### Footnotes / Appendix Cross-References
- Case-sourced expected return decomposition: Appendix A1.
- Drawdown validation: Appendix A2.
- Stress validation: Appendix A3.
- Data integrity and robustness checks: Appendix A6.

---

## APPENDIX — Quantitative Validation & Performance Decomposition
This section provides quantitative validation for the client-facing strategy.

# SLIDE A1 — Return Decomposition + Income Model
### Visual Placement
- No charts (table-only slide).
- Label note: Data sourced from live backtest engine for validation; expected-return assumptions sourced from Case Appendix I/II.

Table caption: Case-sourced decomposition input map (must trace to Appendix I/II rows)
| bucket               | case_fund_reference                                      | source_rule              |
|:---------------------|:---------------------------------------------------------|:-------------------------|
| us_equity            | JPMorgan America Equity Fund (LU0210528500)            | Appendix I/II only       |
| europe_equity        | HSBC GIF Euroland Value Equity (LU1193295406)          | Appendix I/II only       |
| japan_equity         | Pictet Japanese Equity Opportunities (LU0936264273)    | Appendix I/II only       |
| asia_ex_japan_equity | Schroder Asian Equity Yield (LU0188438112)             | Appendix I/II only       |
| global_ig            | HSBC Global IG Securitised Credit (LU1728044204)       | Appendix I/II only       |
| global_hy            | Schroder Global High Yield (LU0418832605)              | Appendix I/II only       |
| em_debt              | Case Appendix best-match fund                            | Appendix I/II only       |
| private_markets      | Case Appendix II private markets/private credit fund     | Appendix II only         |
| hedge_funds          | Case Appendix II Global Multi-Strategy Multi-PM          | Appendix II only         |
| cash                 | Cash proxy assumption (explicitly labeled assumption)    | Assumption + sensitivity |

Table caption: Income decomposition (full portfolio cash-flow model)
| Band   | Total Return %   | Total Return $   | Income Return %   | Income Return $   | Capital Gain %   | Capital Gain $   | Monthly Income $   | vs $25k Requirement   |
|:-------|:-----------------|:-----------------|:------------------|:------------------|:-----------------|:-----------------|:-------------------|:----------------------|
| LOW    | -6.90%           | $-5,519,144      | 4.37%             | $3,492,317        | -11.26%          | $-9,011,461      | $291,026           | MEET                  |
| BASE   | 7.82%            | $6,254,711       | 4.37%             | $3,492,317        | 3.45%            | $2,762,394       | $291,026           | MEET                  |
| HIGH   | 22.54%           | $18,028,567      | 4.37%             | $3,492,317        | 18.17%           | $14,536,249      | $291,026           | MEET                  |

Table caption: Backtest statistics (proxy validation only)
| portfolio     |      cagr |   ann_vol |   sharpe_rf0 |   sharpe_rf_cash |   sortino |   max_drawdown |   calmar |   worst_month |   best_month |   %positive_months |   tracking_error_vs_saa |
|:--------------|----------:|----------:|-------------:|-----------------:|----------:|---------------:|---------:|--------------:|-------------:|-------------------:|------------------------:|
| Current       | 0.111652  | 0.135004  |     0.851856 |         0.689186 |  0.832599 |      -0.260895 | 0.427957 |    -0.0965878 |    0.0886716 |           0.7      |              0.056677   |
| SAA           | 0.0746864 | 0.0969828 |     0.791499 |         0.565056 |  0.662938 |      -0.229063 | 0.326052 |    -0.107193  |    0.0837987 |           0.7      |              0          |
| TAA Static    | 0.0775348 | 0.103578  |     0.77309  |         0.561066 |  0.656544 |      -0.248463 | 0.312058 |    -0.113701  |    0.0884866 |           0.681818 |              0.0100669  |
| TAA Quarterly | 0.0761082 | 0.101401  |     0.774394 |         0.557817 |  0.660098 |      -0.232765 | 0.326974 |    -0.109344  |    0.0870995 |           0.681818 |              0.00712258 |

Income Sustainability Note:
- Income model upgraded to full portfolio cash-flow approach.
- Portfolio income sources: equity dividends, bond coupons, private credit distributions, and cash yield.

# SLIDE A2 — Performance & Drawdown
### Visual Placement
- Figure A2.1 – Growth of +115 lines: outputs/charts/equity_curve.png
- Figure A2.2 – Drawdown Profile: outputs/charts/drawdown.png

# SLIDE A3 — Stress Tests
### Visual Placement
- Figure A3.1 – Scenario Impact Ranking: outputs/charts/stress_bar.png

# SLIDE A4 — Distribution & Rolling Diagnostics
### Visual Placement
- outputs/charts/monthly_return_hist.png
- outputs/charts/sharpe_distribution.png
- outputs/charts/rolling_12m_return.png

# SLIDE A5 — Proxy Mapping & Model Explanation
### Visual Placement
- No charts required (table + methodology box).

# SLIDE A6 — Robustness & Validation
### Visual Placement
- No charts (tables only).

Footnote: Market data sourced via yfinance; adjusted close used; see data coverage table.
