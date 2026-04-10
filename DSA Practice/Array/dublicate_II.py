num = list(map(int,input("Enter numbers: ").split()))

if len(num)<=2:
   print(num)
   print(len(num))

else:
   
  start = 1
  for i in range(1,len(num)):
      if num[i] != num[start-1]:
       start = start+1
       num[start] = num[i]
  print(num[:start+1])
  print(start+1)


