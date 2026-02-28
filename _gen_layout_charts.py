import matplotlib.pyplot as plt
from pathlib import Path

out=Path(r'C:\Users\35882\Desktop\金融tech\openclaw\hsbc_pb_openclaw\outputs\charts')
out.mkdir(parents=True, exist_ok=True)

saa={
'US Equity':15,'Europe Equity':10,'Japan Equity':10,'Asia ex Japan Equity':10,
'Global Investment Grade':15,'Global High Yield':5,'Emerging Market Debt':10,
'Private Markets':12,'Hedge Funds':8,'Cash':5
}
taa={
'US Equity':13,'Europe Equity':10,'Japan Equity':12,'Asia ex Japan Equity':12,
'Global Investment Grade':17,'Global High Yield':3,'Emerging Market Debt':8,
'Private Markets':14,'Hedge Funds':8,'Cash':3
}

def donut(data, fp, title):
    labels=list(data.keys()); vals=list(data.values())
    fig,ax=plt.subplots(figsize=(6,6))
    wedges,_=ax.pie(vals, startangle=90, wedgeprops=dict(width=0.38, edgecolor='white'))
    ax.legend(wedges, [f'{l} ({v}%)' for l,v in zip(labels,vals)], loc='center left', bbox_to_anchor=(1,0.5), fontsize=8)
    ax.set_title(title)
    plt.tight_layout(); fig.savefig(fp, dpi=250); plt.close(fig)

def bar_subset(data, keys, fp, title):
    vals=[data[k] for k in keys]
    fig,ax=plt.subplots(figsize=(7,3.2))
    ax.bar(keys, vals)
    ax.set_ylim(0,max(vals)+5)
    ax.set_ylabel('Weight (%)')
    ax.set_title(title)
    plt.xticks(rotation=20, ha='right')
    plt.tight_layout(); fig.savefig(fp,dpi=250); plt.close(fig)

donut(saa, out/'saa_donut.png', 'SAA Weights')
donut(taa, out/'taa_donut.png', 'TAA Weights')
bar_subset(saa, ['US Equity','Europe Equity','Japan Equity','Asia ex Japan Equity'], out/'equity_region_bar_saa.png', 'SAA Equity Regional Weights')
bar_subset({'Global Investment Grade':15,'Global High Yield':5,'Emerging Market Debt':10,'Cash':5}, ['Global Investment Grade','Global High Yield','Emerging Market Debt','Cash'], out/'fi_bucket_bar_saa.png', 'SAA Fixed Income / Cash Buckets')
print('charts generated')
