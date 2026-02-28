import numpy as np, pandas as pd, yaml
from pathlib import Path
root=Path(r'C:\Users\35882\Desktop\金融tech\openclaw\hsbc_pb_openclaw')
cfg=yaml.safe_load(open(root/'config'/'config.yaml',encoding='utf-8'))
# load bucket daily returns from live proxy
r=pd.read_csv(root/'outputs'/'tables'/'bucket_daily_returns.csv',index_col=0,parse_dates=True)
# correlation from empirical data
corr=r.corr()
# case vol inputs (annual, decimal)
vol={
'us_equity':0.156,
'europe_equity':0.167,
'japan_equity':0.124,
'asia_ex_japan_equity':0.167,
'global_ig':0.020,
'global_hy':0.069,
'em_debt':0.098,
'private_markets':0.196,
'hedge_funds':0.068,
'cash':0.005,
}
assets=list(vol)
D=np.diag([vol[a] for a in assets])
C=corr.loc[assets,assets].values
Sigma=D@C@D
for name,key in [('SAA','saa'),('TAA','taa_static')]:
    w=np.array([cfg['weights'][key][a] for a in assets])
    vp=float(np.sqrt(w@Sigma@w))
    print(name, vp)
