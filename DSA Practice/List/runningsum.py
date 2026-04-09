num = list(map(int,input("Enter numbers: ").split()))
running_sum = []
ans = 0
for i in num:
    ans = ans + i
    running_sum.append(ans)
print(running_sum)    