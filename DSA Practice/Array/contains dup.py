num = list(map(int,input("Enter number: ").split()))
if len(num)!= len(set(num)):
    print(True)
else:
    print(False)    