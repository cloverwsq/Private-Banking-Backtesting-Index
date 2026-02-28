import pdfplumber, pathlib, pandas as pd
p=pathlib.Path(r'inputs/HSBC PB Case Challenge 2026 Qualifier Round Case.pdf')
out=pathlib.Path('outputs/tables/case_tables_dump'); out.mkdir(parents=True, exist_ok=True)
with pdfplumber.open(p) as pdf:
    for i,pg in enumerate(pdf.pages,1):
        tabs=pg.extract_tables()
        for j,t in enumerate(tabs,1):
            df=pd.DataFrame(t)
            fp=out/f'p{i}_t{j}.csv'
            df.to_csv(fp,index=False,header=False)
print('done')
