def sumoftwo(n):
    if n == 1:
        return True
    if n%2!=0:
        return False
    return sumoftwo(n=n//2)

print(sumoftwo(8))

      