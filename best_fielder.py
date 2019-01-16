try:
    import pandas as pd
except ImportError:
    print('Pandas Library not Installed ! Install pandas and try again')
def field():
    delivery=pd.read_csv('deliveries.csv')
    print('''Menu:
            1)Best Fielder(Catches per Match)
            2)Best Fielder(Catches per Over)''')
    ch=int(input("Enter Choice:"))
    if(ch==1):
        a=delivery.groupby('fielder')['fielder'].count()
        b=delivery.groupby('fielder')['match_id'].nunique()
        c=a/b
        print(c.sort_values(ascending=False).head(5))
    elif(ch==2):
        a=delivery.groupby('fielder')['fielder'].count()
        b=delivery.groupby('fielder')['ball'].count()/6
        c=a/b
        print(c.sort_values(ascending=False).head(5))

