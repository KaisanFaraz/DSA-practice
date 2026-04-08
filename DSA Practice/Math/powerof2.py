def sumoftwo(n):
    while n%2==0:
        n//=2
        
    if n==1:
        return True
    else:
        return False
print(sumoftwo(8))            