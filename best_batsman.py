try:
    import pandas as pd
except ImportError:
    print('Pandas Library not Installed ! Install pandas and try again')
delivery=pd.read_csv('deliveries.csv')
delivery['batsman'].nunique() 
x=delivery['batsman'].value_counts()>200 
y=x[x].index.tolist()
mask=delivery['batsman'].isin(y) 
new_delivery=delivery[mask]
mask=new_delivery['over']>15
mew_delivery=new_delivery[mask]
a=mew_delivery.groupby('batsman')['batsman_runs'].sum()
b=mew_delivery.groupby('batsman')['batsman_runs'].count()
c=a/b
c*=100
print(c.sort_values(ascending=False))
