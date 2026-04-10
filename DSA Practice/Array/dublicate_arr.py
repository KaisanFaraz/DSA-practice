num = list(map(int,input("Enter numbers: ").split()))
start = 0
for i in range(1,len(num)):
     if num[i] != num[start]:
      start = start+1
      num[start] = num[i]
print(num[:start+1])
print(start+1)


