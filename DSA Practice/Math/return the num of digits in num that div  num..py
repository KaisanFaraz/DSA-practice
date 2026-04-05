n = int(input("Enter a number: "))
temp = n
ans = 0
while temp > 0:
    r = temp % 10
    
    if temp%r==0:
        ans = ans+1
    
    temp //= 10
print(ans)