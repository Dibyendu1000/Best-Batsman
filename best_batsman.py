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
while(1):
    print('''Menu:
          1)Best Batsman (Best Strike Rate)
          2)Best Batsman (Best Avg Runs)
          3)Best Batsman (Longest Survival)
          4)Exit''')
    ch=int(input("Enter Choice:"))
    if(ch==1):
        a=mew_delivery.groupby('batsman')['batsman_runs'].sum()
        b=mew_delivery.groupby('batsman')['batsman_runs'].count()/6
        c=a/b
        print(c.sort_values(ascending=False).head(5))
    elif(ch==2):
        a=mew_delivery.groupby('batsman')['batsman_runs'].sum()
        b=mew_delivery.groupby('batsman')['match_id'].nunique()
        c=a/b
        print(c.sort_values(ascending=False).head(5))
    elif(ch==3):
        a=mew_delivery.groupby('batsman')['batsman_runs'].count()/6
        b=mew_delivery.groupby('batsman')['match_id'].nunique()
        c=a/b
        print(c.sort_values(ascending=False).head(5))
    elif(ch==4):
        exit()
