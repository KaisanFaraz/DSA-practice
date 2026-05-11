price = list(map(int,input("Enter price:").split()))
min_p = price[0]
max_profit = 0

for i in range(len(price)):
    if price[i]< min_p:
        min_p = price[i]
    cur_profit = price[i]- min_p
    if max_profit < cur_profit:
        max_profit = cur_profit
print(max_profit)            
