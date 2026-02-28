from __future__ import annotations
import argparse
from pathlib import Path
import re
import pandas as pd

CASE_FUNDS = [
    ("US Equity", "JPMorgan America Equity Fund", "LU0210528500", "Appendix I"),
    ("Europe Equity", "HSBC GIF Euroland Value Equity", "LU1193295406", "Appendix I"),
    ("Japan Equity", "Pictet Japanese Equity Opportunities", "LU0936264273", "Appendix I"),
    ("Asia ex-Japan Equity", "Schroder Asian Equity Yield", "LU0188438112", "Appendix I"),
    ("Global IG", "HSBC Global IG Securitised Credit", "LU1728044204", "Appendix I"),
    ("Global HY", "Schroder Global High Yield", "LU0418832605", "Appendix I"),
    ("EM Debt", "Best match from Appendix I/II", "N/A", "Appendix I/II"),
    ("Private Markets", "Private Markets/Private Credit representative", "N/A", "Appendix II"),
    ("Hedge Funds", "Global Multi-Strategy Multi-PM", "N/A", "Appendix II"),
]

def main():
    p = argparse.ArgumentParser()
    p.add_argument('--case', required=True)
    args = p.parse_args()
    out = Path(__file__).resolve().parents[1] / 'data' / 'processed'
    out.mkdir(parents=True, exist_ok=True)

    df = pd.DataFrame(CASE_FUNDS, columns=['bucket', 'fund_name', 'identifier', 'appendix_source'])
    df['note'] = 'Use case Appendix I/II values manually validated from case PDF.'
    df.to_csv(out / 'case_fund_representatives.csv', index=False)

    # lightweight trace file
    txt = Path(args.case)
    extracted = ''
    try:
        import pdfplumber
        with pdfplumber.open(txt) as pdf:
            for page in pdf.pages[:6]:
                t = page.extract_text() or ''
                extracted += t + '\n'
    except Exception as e:
        extracted = f'pdf extraction skipped: {e}'
    (out / 'case_extract_trace.txt').write_text(extracted[:5000], encoding='utf-8')
    print(f'wrote {out / "case_fund_representatives.csv"}')

if __name__ == '__main__':
    main()
