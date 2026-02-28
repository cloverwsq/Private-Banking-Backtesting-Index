import pdfplumber, pathlib
p=pathlib.Path(r'inputs/HSBC PB Case Challenge 2026 Qualifier Round Case.pdf')
with pdfplumber.open(p) as pdf:
    for i in range(7,12):
        pg=pdf.pages[i-1]
        print(f'\n==== PAGE {i} ====')
        t=pg.extract_text() or ''
        print(t[:7000])
