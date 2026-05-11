num = list(map(int,input("Enter number:").split()))
cur_sum = 0
max_sum = num[0]
for i in num:
    cur_sum = cur_sum+num[i]
    if cur_sum>max_sum:
        max_sum = cur_sum
    if cur_sum<0:
        cur_sum = 0
print(max_sum)            