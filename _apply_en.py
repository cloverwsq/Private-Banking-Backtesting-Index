from pathlib import Path
p=Path(r'C:\Users\35882\Desktop\金融tech\openclaw\hsbc_pb_openclaw\outputs\slide_content.md')
t=p.read_text(encoding='utf-8')
old="""### LEFT PANEL — Education Planning
- Timeline: Age 5 today → University starts in year 13.
- Education objective is embedded in total portfolio now; no separate trust is set up today.
- Funding logic: 4-year university schedule, inflation-adjusted nominal costs, discounted to present value.
"""
new="""### LEFT PANEL — Education Funding Governance Framework (Liability-First)
- Today (Age 5): keep education embedded within the total portfolio, while formalizing an Education Liability Schedule + PV framework and setting a glide path (strategy locked, structure not locked).
- Trigger (Age ~9–12): when remaining horizon falls below ~8–10 years, progressively de-risk the education sleeve toward Global IG and cash-like assets for liability matching.
- Optional legal structure (Age ~12+): if isolation, succession, or cross-border governance needs become binding, consider establishing an education trust and transferring the de-risked sleeve.
- One-line conclusion: first make funding sufficiency auditable through liability matching; then decide whether trust structuring is necessary.
"""
if old in t:
    t=t.replace(old,new)
t=t.replace('materially exceeds average annual university cost (487,643); liability is covered.','materially exceeds average annual university cost (487,643), indicating funded status under current assumptions.')
p.write_text(t,encoding='utf-8')
print('updated')
