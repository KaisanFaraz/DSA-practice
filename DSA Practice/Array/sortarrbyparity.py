num = list(map(int,input("Enter numbers: ").split()))
start = 0
for i in range(0,len(num)):
    if num[i] % 2== 0:
        temp = num[i]
        num[i] = num[start]
        num[start] = temp
        start = start+1
print(num)        
