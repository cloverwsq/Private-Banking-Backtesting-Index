from __future__ import annotations
import yaml
from pathlib import Path

EQUITY_BUCKETS = {'us_equity','europe_equity','japan_equity','asia_ex_japan_equity'}
ALTERNATIVE_BUCKETS = {'private_markets','hedge_funds'}

RATIONALES = {
    'SPY': ('US large-cap beta proxy', 'fund-level style drift not captured'),
    'VGK': ('Europe developed equity proxy', 'currency and factor mismatch'),
    'EWJ': ('Japan equity beta proxy', 'active manager alpha not captured'),
    'AIA': ('Asia ex-Japan equity proxy', 'regional composition mismatch'),
    'AGG': ('Global/US IG duration-credit blend', 'not exact securitised credit mix'),
    'HYG': ('Global HY beta proxy', 'issuer-quality mix differs from case fund'),
    'EMB': ('USD EM sovereign debt proxy', 'local debt/active selection not captured'),
    'BIZD': ('Listed private credit/BDC proxy', 'listed beta differs from private NAV smoothing'),
    'BTAL': ('Conservative alternative/risk-hedge proxy', 'not a true multi-PM hedge fund replication'),
    'BIL': ('Cash/T-bill proxy', 'cash account rates may differ')
}

def load_config(config_path: str | Path):
    with open(config_path, 'r', encoding='utf-8') as f:
        return yaml.safe_load(f)

def build_mapping_df(cfg):
    import pandas as pd
    rows = []
    for b, t in cfg['proxy_map'].items():
        r, l = RATIONALES.get(t, ('Liquid tradable proxy', 'mapping approximation'))
        rows.append({'bucket': b, 'proxy': t, 'rationale': r, 'limitation': l})
    return pd.DataFrame(rows)
