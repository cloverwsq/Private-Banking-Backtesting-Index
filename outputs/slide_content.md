## CLIENT SLIDES

# SLIDE 1 — Education Objective Embedded Within Total Portfolio
Title: Liability-Aligned Education Planning (Age 5 to University in ~13 Years)

### LEFT PANEL — Education Funding Governance Framework (Liability-First)
- Today (Age 5): keep education embedded within the total portfolio, while formalizing an Education Liability Schedule + PV framework and setting a glide path (strategy locked, structure not locked).
- Trigger (Age ~9–12): when remaining horizon falls below ~8–10 years, progressively de-risk the education sleeve toward Global IG and cash-like assets for liability matching.
- Optional legal structure (Age ~12+): if isolation, succession, or cross-border governance needs become binding, consider establishing an education trust and transferring the de-risked sleeve.
- One-line conclusion: first make funding sufficiency auditable through liability matching; then decide whether trust structuring is necessary.

Table caption: Education Liability Schedule (C0=240,000; inflation=5.0%; discount rate=3.5%; start in year 13)
| Year | Projected Cost (Nominal) | Discount Factor | Present Value |
|:--|--:|--:|--:|
| Year 1 of university (k=13) | 452,556 | 0.6394 | 289,366 |
| Year 2 of university (k=14) | 475,184 | 0.6178 | 293,560 |
| Year 3 of university (k=15) | 498,943 | 0.5969 | 297,814 |
| Year 4 of university (k=16) | 523,890 | 0.5767 | 302,130 |
| Total | 1,950,572 | - | 1,182,870 |

Coverage statement:
- Under BASE case cash-flow capacity, annual portfolio income (SAA: 3,188,000; TAA: 3,240,800) materially exceeds average annual university cost (487,643), indicating funded status under current assumptions.

### RIGHT PANEL — Portfolio Response
- Glide-path framework (conceptual):
  - Phase 1 (Age 5–8): growth-oriented mix
  - Phase 2 (Age 9–12): gradual increase in Global IG
  - Phase 3 (Age 13–17): majority IG to immunize near-dated liability

Table caption: SAA Allocation (Current Strategic Mix)
| Asset/Sub-asset | Weight % |
|:--|--:|
| US Equity | 15.0 |
| Europe Equity | 10.0 |
| Japan Equity | 10.0 |
| Asia ex Japan Equity | 10.0 |
| Global Investment Grade | 15.0 |
| Global High Yield | 5.0 |
| Emerging Market Debt | 10.0 |
| Private Markets | 12.0 |
| Hedge Funds | 8.0 |
| Cash | 5.0 |

Table caption: SAA Key Metrics (Case-Derived)
| Metric | BASE |
|:--|--:|
| Expected Return | 9.60% |
| Volatility | 8.58% |
| Income Yield | 3.99% |

### Visual Placement
- Left panel: education timeline + liability table.
- Right panel: `outputs/charts/saa_donut.png` + SAA key metrics mini-table.
- No historical backtest charts on this slide.

### Footnotes / Compliance
- Client-slide forward-looking metrics are derived from case inputs only.
- Historical validation/backtest content is Appendix-only.

---

# SLIDE 2 — Strategic and Tactical Asset Allocation
Title: Portfolio Construction with Disciplined Tactical Overlay

### TOP PANEL — Portfolio Construction
Table caption: Tactical Adjustments (SAA vs TAA)
| Asset | SAA | TAA | Delta |
|:--|:--|:--|:--|
| Asia ex Japan Equity | 10.0% | 12.0% | +2.0% |
| Cash | 5.0% | 3.0% | -2.0% |
| Emerging Market Debt | 10.0% | 8.0% | -2.0% |
| Europe Equity | 10.0% | 10.0% | +0.0% |
| Global High Yield | 5.0% | 3.0% | -2.0% |
| Global Investment Grade | 15.0% | 17.0% | +2.0% |
| Hedge Funds | 8.0% | 8.0% | +0.0% |
| Japan Equity | 10.0% | 12.0% | +2.0% |
| Private Markets | 12.0% | 14.0% | +2.0% |
| US Equity | 15.0% | 13.0% | -2.0% |

Table caption: SAA vs TAA KPI Summary (Case-Derived)
| Portfolio | Expected Return (LOW) | Expected Return (BASE) | Expected Return (HIGH) | Volatility | Expected Yield |
|:--|--:|--:|--:|--:|--:|
| SAA | -1.86% | 9.60% | 21.07% | 8.58% | 3.99% |
| TAA | -1.88% | 9.95% | 21.77% | 8.81% | 4.05% |
| Delta (TAA-SAA, pp) | -0.01pp | +0.34pp | +0.70pp | +0.23pp | +0.07pp |

### BOTTOM PANEL — Positioning
Equity positioning (weights-based):
- Regional equity exposure is balanced across US, Europe, Japan, and Asia ex-Japan.
- TAA rotates modestly toward Japan and Asia ex-Japan while trimming US.

Fixed income positioning (weights-based):
- TAA tilts toward higher Global IG and trims HY + EM debt marginally.
- Cash is reduced tactically to fund risk-controlled return enhancement.

Portfolio emphasizes:
- Growth aligned with 13-year horizon.
- Income sustainability above required threshold.
- Diversified multi-asset exposures with private markets and alternatives.

### Visual Placement
- Top-left: `outputs/charts/saa_donut.png`
- Top-middle: `outputs/charts/taa_donut.png`
- Top-right: KPI summary table
- Bottom-left: `outputs/charts/equity_region_bar_saa.png`
- Bottom-right: `outputs/charts/fi_bucket_bar_saa.png`

### Footnotes / Compliance
- No ratings/sector/duration/YTM breakdown shown because not explicitly provided in case tables.
- Full decomposition and validation references: Appendix A2–A8.

---

## APPENDIX — Quantitative Validation & Methodology
This section provides quantitative validation for the client-facing strategy.

Discount factor methodology:
- DF_k = 1 / (1 + r)^k, with r = 3.5%.
- DF_13 = 1/(1.035)^13 = 0.6394
- DF_14 = 1/(1.035)^14 = 0.6178
- DF_15 = 1/(1.035)^15 = 0.5969
- DF_16 = 1/(1.035)^16 = 0.5767
- PV_k = NominalCost_k × DF_k
Table caption: Education Liability Schedule (Assumptions: C0=240,000; education inflation=5.0%; discount rate=3.5%; horizon starts in year 13)
| Year | Projected Cost (Nominal) | Discount Factor | Present Value |
|:--|--:|--:|--:|
| Year 1 of university (k=13) | 452,556 | 0.6394 | 289,366 |
| Year 2 of university (k=14) | 475,184 | 0.6178 | 293,560 |
| Year 3 of university (k=15) | 498,943 | 0.5969 | 297,814 |
| Year 4 of university (k=16) | 523,890 | 0.5767 | 302,130 |
| Total | 1,950,572 | - | 1,182,870 |

Table caption: Education Funding Coverage Test (No Allocation Change)
| Metric | SAA | TAA |
|:--|--:|--:|
| Annual portfolio income | 3,188,000 | 3,240,800 |
| Average annual university cost | 487,643 | 487,643 |
| Coverage multiple | 6.54x | 6.65x |
| Coverage conclusion | Covered | Covered |

# SLIDE A2 — Income Calculation Methodology (Case-Based)
Table caption: Income Model Formulae
| Component | Formula | Value |
|:--|:--|:--|
| Portfolio Income Yield | Σ(wi × income component_i) | SAA: 3.99%; TAA: 4.05% |
| Annual Income | Income Yield × AUM | SAA: 3,188,000; TAA: 3,240,800 |
| Monthly Income | Annual Income / 12 | SAA: 265,667; TAA: 270,067 |
| Required Yield | 300,000 / AUM | 0.375% |
| Coverage Ratio | Monthly Income / 25,000 | SAA: 10.63x; TAA: 10.80x |

Table caption: Income Component Inputs by Asset Class
| Asset Class | Income Component (Case) |
|:--|--:|
| Equities | 2.8% |
| Fixed Income | 4.5% |
| Alternatives | 6.5% |
| Cash | 1.5% |

# SLIDE A3 — Expected Return Decomposition (Case Inputs)
Table caption: Bucket-Level Return / Volatility Inputs and Contributions (SAA)
| Bucket | Weight | Representative Fund (Case) | Return | Volatility | BASE Contribution |
|:--|--:|:--|--:|--:|--:|
| US Equity | 15.0% | JPMorgan America Equity Fund (LU0210528500) | 14.4% | 15.6% | 2.16% |
| Europe Equity | 10.0% | HSBC GIF Euroland Value Equity (LU1193295406) | 16.5% | 16.7% | 1.65% |
| Japan Equity | 10.0% | Pictet Japanese Equity Opportunities (LU0936264273) | 18.0% | 12.4% | 1.80% |
| Asia ex Japan Equity | 10.0% | Schroder Asian Equity Yield (LU0188438112) | 8.7% | 16.7% | 0.87% |
| Global Investment Grade | 15.0% | HSBC Global IG Securitised Credit (LU1728044204) | 3.5% | 2.0% | 0.53% |
| Global High Yield | 5.0% | Schroder Global High Yield (LU0418832605) | 3.8% | 6.9% | 0.19% |
| Emerging Market Debt | 10.0% | BlackRock Emerging Markets Bond (LU0200680600) | 3.2% | 9.8% | 0.32% |
| Private Markets | 12.0% | Global Private Equity Fund (Appendix II) | 9.9% | 19.6% | 1.19% |
| Hedge Funds | 8.0% | Global Multi-Strategy Multi-PM (Appendix II) | 10.3% | 6.8% | 0.82% |
| Cash | 5.0% | Case cash assumption | 1.5% | 0.5% | 0.08% |

Table caption: Portfolio Outputs from Case Inputs
| Portfolio | Expected Return (LOW) | Expected Return (BASE) | Expected Return (HIGH) | Volatility |
|:--|--:|--:|--:|--:|
| SAA | -1.86% | 9.60% | 21.07% | 8.58% |
| TAA | -1.88% | 9.95% | 21.77% | 8.81% |

Volatility Reconciliation Note:
- Current volatility figures (SAA 8.58%, TAA 8.81%) use case bucket vol with empirical cross-asset correlation estimated from live proxy history.
- If official full case covariance matrix is provided, rerun sigma = sqrt(w^T Sigma w) and overwrite final volatility lock values.

# SLIDE A4 — Proxy Mapping Table (Validation Only)
Table caption: Historical Validation Proxy Mapping (Not Used for Forward Assumptions)
| Case Bucket | Validation Proxy |
|:--|:--|
| US Equity | SPY |
| Europe Equity | VGK |
| Japan Equity | EWJ |
| Asia ex Japan Equity | AIA |
| Global Investment Grade | AGG |
| Global High Yield | HYG |
| Emerging Market Debt | EMB |
| Private Markets | BIZD |
| Hedge Funds | BTAL |
| Cash | BIL |

# SLIDE A5 — Backtest Metrics (Validation Only)
Visual Placement:
- outputs/charts/equity_curve.png (Top panel)
- outputs/charts/drawdown.png (Second panel)
- outputs/charts/rolling_12m_return.png (Bottom-left)
- outputs/charts/monthly_return_hist.png (Bottom-middle)
- outputs/charts/sharpe_distribution.png (Bottom-right)

Table caption: Historical Validation Metrics (Proxy-Based)
| portfolio | cagr | ann_vol | sharpe_rf0 | sharpe_rf_cash | sortino | max_drawdown | calmar | worst_month | best_month | %positive_months | tracking_error_vs_saa |
|:--|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Current | 0.111652 | 0.135004 | 0.851856 | 0.689186 | 0.832599 | -0.260895 | 0.427957 | -0.0965878 | 0.0886716 | 0.7 | 0.056677 |
| SAA | 0.0746864 | 0.0969828 | 0.791499 | 0.565056 | 0.662938 | -0.229063 | 0.326052 | -0.107193 | 0.0837987 | 0.7 | 0 |
| TAA Static | 0.0775348 | 0.103578 | 0.77309 | 0.561066 | 0.656544 | -0.248463 | 0.312058 | -0.113701 | 0.0884866 | 0.681818 | 0.0100669 |
| TAA Quarterly | 0.0761082 | 0.101401 | 0.774394 | 0.557817 | 0.660098 | -0.232765 | 0.326974 | -0.109344 | 0.0870995 | 0.681818 | 0.00712258 |

# SLIDE A6 — Stress Tests (Validation Only)
Visual Placement:
- outputs/charts/stress_bar.png (Figure A6.1 — Scenario Impact Ranking)

Table caption: Historical Stress Windows
| window | portfolio | cum_return | peak_to_trough_dd | recovery_days |
|:--|:--|--:|--:|--:|
| covid | Current | -0.107027 | -0.260103 | nan |
| covid | SAA | -0.103562 | -0.228479 | nan |
| covid | TAA Static | -0.108542 | -0.247634 | nan |
| covid | TAA Quarterly | -0.104713 | -0.231965 | nan |
| rates_2022 | Current | -0.16156 | -0.210017 | nan |
| rates_2022 | SAA | -0.170225 | -0.200675 | nan |
| rates_2022 | TAA Static | -0.174344 | -0.205101 | nan |
| rates_2022 | TAA Quarterly | -0.176026 | -0.207391 | nan |
| q4_2018 | Current | -0.104425 | -0.144511 | nan |
| q4_2018 | SAA | -0.0675693 | -0.0888146 | nan |
| q4_2018 | TAA Static | -0.0713516 | -0.0933128 | nan |
| q4_2018 | TAA Quarterly | -0.0741509 | -0.0958279 | nan |

# SLIDE A7 — Data Coverage
Visual Placement:
- No chart (table-only)

Table caption: Live Validation Data Coverage (yfinance)
| ticker | start_date | end_date | coverage_pct | missing_days_pct | source |
|:--|:--|:--|--:|--:|:--|
| AGG | 2017-01-03 | 2026-02-27 | 96.3165 | 3.68355 | yfinance |
| AIA | 2017-01-03 | 2026-02-27 | 96.3165 | 3.68355 | yfinance |
| BIL | 2017-01-03 | 2026-02-27 | 96.3165 | 3.68355 | yfinance |
| BIZD | 2017-01-03 | 2026-02-27 | 96.3165 | 3.68355 | yfinance |
| BTAL | 2017-01-03 | 2026-02-27 | 96.3165 | 3.68355 | yfinance |
| EMB | 2017-01-03 | 2026-02-27 | 96.3165 | 3.68355 | yfinance |
| EWJ | 2017-01-03 | 2026-02-27 | 96.3165 | 3.68355 | yfinance |
| HYG | 2017-01-03 | 2026-02-27 | 96.3165 | 3.68355 | yfinance |
| SPY | 2017-01-03 | 2026-02-27 | 96.3165 | 3.68355 | yfinance |
| VGK | 2017-01-03 | 2026-02-27 | 96.3165 | 3.68355 | yfinance |

# SLIDE A8 — Transaction Cost Sensitivity
Visual Placement:
- No chart (table-only)

Table caption: Turnover Cost Sensitivity (Validation Only)
| tc_bps | portfolio | cagr | sharpe_rf_cash | max_drawdown |
|--:|:--|--:|--:|--:|
| 0 | Current | 0.111829 | 0.690377 | -0.260895 |
| 0 | SAA | 0.0749198 | 0.567313 | -0.229063 |
| 0 | TAA Static | 0.0775348 | 0.561066 | -0.248463 |
| 0 | TAA Quarterly | 0.0762465 | 0.559093 | -0.232765 |
| 10 | Current | 0.111652 | 0.689186 | -0.260895 |
| 10 | SAA | 0.0746864 | 0.565056 | -0.229063 |
| 10 | TAA Static | 0.0775348 | 0.561066 | -0.248463 |
| 10 | TAA Quarterly | 0.0761082 | 0.557817 | -0.232765 |
| 25 | Current | 0.111386 | 0.6874 | -0.260895 |
| 25 | SAA | 0.0743363 | 0.56167 | -0.229063 |
| 25 | TAA Static | 0.0775348 | 0.561066 | -0.248463 |
| 25 | TAA Quarterly | 0.0759009 | 0.555903 | -0.232765 |

Disclosure:
Historical data used solely for robustness validation. Forward-looking assumptions derived exclusively from case inputs.



# SLIDE A9 — Portfolio Backtesting & Downside Risk Analysis
Title: Portfolio Backtesting & Downside Risk Analysis

### Top Left — Risk Matrix (Portfolio-Specific)
| Risk Category | Portfolio-Specific Manifestation | Current Control |
|:--|:--|:--|
| Equity beta drawdown | Equity sleeve can drive short-term mark-to-market losses | Diversified regional equity + alternatives |
| Credit spread widening | HY/EM debt spread shock can reduce near-term valuation | IG anchor + limited HY weight |
| Liquidity mismatch | Private markets are less liquid than public sleeves | Cash + listed liquid sleeves for near-term needs |
| Sequence risk (education horizon) | Adverse window before liability dates | Glide-path trigger (8–10y to liability) |
| Tactical drift risk | Overlay can add unintended risk | ±2% tactical bands and periodic rebalance |


### Top Right — Monte Carlo Distribution (BASE: mu=9.6%, sigma=8.6%, horizon=13y, AUM=80m)
Visual Placement:
- outputs/charts/monte_carlo_terminal_wealth.png (Figure A9.1 — Terminal Wealth Distribution, USD mn)

Table caption: Terminal Wealth Percentiles (USD mn)
| percentile   |   terminal_wealth_usd_mn |
|:-------------|-------------------------:|
| p1           |                   130.44 |
| p5           |                   159.59 |
| p10          |                   178.02 |
| p25          |                   215.01 |
| p50          |                   265.78 |
| p75          |                   326.78 |
| p90          |                   395.14 |
| p95          |                   440.89 |
| p99          |                   548.24 |

Funding probability statement:
- Education PV liability reference: USD 1.18mn.
- Probability of terminal wealth >= education PV: 100.00%.

### Bottom Left — Historical VaR Summary (95%)
Table caption: 1-day and 10-day Historical VaR
| portfolio     | VaR_1d_95   | VaR_10d_95   |
|:--------------|:------------|:-------------|
| SAA           | 0.86%       | 2.42%        |
| TAA Static    | 0.90%       | 2.58%        |
| TAA Quarterly | 0.91%       | 2.64%        |
| Current       | 1.25%       | 3.66%        |

### Bottom Right — Scenario Analysis (Historical Windows)
Table caption: COVID / rates_2022 / q4_2018 outcomes
| window     | portfolio     | cum_return   | peak_to_trough_dd   |
|:-----------|:--------------|:-------------|:--------------------|
| covid      | Current       | -10.70%      | -26.01%             |
| covid      | SAA           | -10.36%      | -22.85%             |
| covid      | TAA Static    | -10.85%      | -24.76%             |
| covid      | TAA Quarterly | -10.47%      | -23.20%             |
| rates_2022 | Current       | -16.16%      | -21.00%             |
| rates_2022 | SAA           | -17.02%      | -20.07%             |
| rates_2022 | TAA Static    | -17.43%      | -20.51%             |
| rates_2022 | TAA Quarterly | -17.60%      | -20.74%             |
| q4_2018    | Current       | -10.44%      | -14.45%             |
| q4_2018    | SAA           | -6.76%       | -8.88%              |
| q4_2018    | TAA Static    | -7.14%       | -9.33%              |
| q4_2018    | TAA Quarterly | -7.42%       | -9.58%              |

Narrative:
- Volatility remains controlled relative to growth objective under the strategic design.
- Education PV liability (1.18mn) is immaterial versus total AUM (80mn).
- Tactical overlay improves opportunity set without materially increasing tail-risk profile.
