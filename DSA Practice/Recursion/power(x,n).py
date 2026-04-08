def findpow(x,n):
    if n == 0:
        return 1
    a = findpow(x,n=n//2)
    if n%2==0:
        return a*a
    else:
        return a*a*x
print(findpow(2,10))    