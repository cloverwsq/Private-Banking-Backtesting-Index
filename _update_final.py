from pathlib import Path
p=Path(r'C:\Users\35882\Desktop\金融tech\openclaw\hsbc_pb_openclaw\outputs\slide_content.md')
t=p.read_text(encoding='utf-8')

old1='''Income Sustainability Note:
- Required portfolio yield to meet target income: 0.375%.
- BASE income yield: 3.99%.
- Coverage is above required level under the case-based income framework.
'''
new1='''Income Sustainability Note:
- Required portfolio yield to meet target income: 0.375%.
- BASE income yield: 3.99%.
- Education affordability check: SAA annual income (3,188,000) covers average annual university cost (487,643) by 6.54x.
- TAA annual income (3,240,800) covers average annual university cost (487,643) by 6.65x.
'''
t=t.replace(old1,new1)

old2='''# SLIDE A1 �� Education Liability Calculation
Table caption: Education Liability Schedule Framework
| Year | Projected Cost (Nominal) | Discount Factor | Present Value |
|:--|:--|:--|:--|
| Year 1 of university | Case-derived | Case-derived | Case-derived |
| Year 2 of university | Case-derived | Case-derived | Case-derived |
| Year 3 of university | Case-derived | Case-derived | Case-derived |
| Year 4 of university | Case-derived | Case-derived | Case-derived |
| Total | Case-derived | - | Education Liability PV |
'''
new2='''# SLIDE A1 �� Education Liability Calculation
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
'''
t=t.replace(old2,new2)

t=t.replace('Volatility Reconciliation Note:\n- Current volatility figures (SAA 4.43%, TAA 4.66%) are preliminary case-volatility outputs using a simplified covariance structure.\n- Final volatility must be revalidated against the full official case covariance/correlation matrix before submission freeze.\n','Volatility Reconciliation Note:\n- Current volatility figures (SAA 8.58%, TAA 8.81%) use case bucket vol with empirical cross-asset correlation estimated from live proxy history.\n- If official full case covariance matrix is provided, rerun sigma = sqrt(w^T Sigma w) and overwrite final volatility lock values.\n')

p.write_text(t,encoding='utf-8')
print('updated')
