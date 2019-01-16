import pandas as pd
import best_batsman
import best_bowler
import best_fielder
delivery=pd.read_csv('deliveries.csv')
while(1):
    print('''Menu
            1)Best Batsman
            2)Best Bowler
            3)Best Fielder
            4)Exit''')
    ch=int(input("Enter Choice:"))
    if(ch==1):
          best_batsman.bat()
    elif(ch==2):
          best_bowler.ball()
    elif(ch==3):
          best_fielder.field()
    elif(ch==4):
          exit()
    else:
          print('Invalid Input')
