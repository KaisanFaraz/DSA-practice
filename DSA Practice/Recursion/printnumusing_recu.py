def printnum(i,n):
    if i>n:
        return
    print(i,end=" ")
    printnum(i+1,n)
printnum(1,10)    
    