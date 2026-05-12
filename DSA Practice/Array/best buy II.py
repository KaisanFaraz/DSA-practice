price = list(map(int,input("Enter price: ").split()))
max_profit = 0 
for i in range(1,len(price)):
    if price[i]>price[i-1] :
        max_profit = max_profit + (price[i] - price[i-1])
print(max_profit)    
