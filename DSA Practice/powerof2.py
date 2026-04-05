n=int(input())
if n>0:
    while n%2 ==0:
        n//=2
if n==1:
    print("Yes")      
else:
    print("No")      