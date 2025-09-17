balance =500
while balance >=100:
    print("current balance:",balance)
    withdraw=int(input("Enter amount to withdraw:"))
    
    if withdraw<=balance:
        balance-=withdraw
        print("withrrawal successful! new balance:",balance)
    else:
         print("Not enough balance to withdraw that amount.")
print("low balance -transection stopped")
        
    