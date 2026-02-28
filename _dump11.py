import pdfplumber, pathlib, json
p=pathlib.Path(r'inputs/HSBC PB Case Challenge 2026 Qualifier Round Case.pdf')
out=pathlib.Path('outputs/tables/page11_dump.txt')
with pdfplumber.open(p) as pdf:
    pg=pdf.pages[10]
    t=pg.extract_text() or ''
    out.write_text(t,encoding='utf-8')
    tabs=pg.extract_tables()
    pathlib.Path('outputs/tables/page11_tables.json').write_text(json.dumps(tabs,ensure_ascii=False,indent=2),encoding='utf-8')
print('saved')
