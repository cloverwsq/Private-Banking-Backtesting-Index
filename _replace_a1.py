from pathlib import Path
p=Path(r'C:\Users\35882\Desktop\金融tech\openclaw\hsbc_pb_openclaw\outputs\slide_content.md')
t=p.read_text(encoding='utf-8')
start=t.index('# SLIDE A1')
end=t.index('# SLIDE A2')
new='''# SLIDE A1 — Education Liability Calculation
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
t=t[:start]+new+t[end:]
p.write_text(t,encoding='utf-8')
print('A1 replaced')
