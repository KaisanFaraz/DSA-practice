n = int(input("Enter number: "))
temp = n
sum = 0
prod = 1
while temp > 0:   #234 input
    r = temp%10    #4
    temp //=10     #23    4 left
    sum =sum +r    #4 add
    prod = prod *r  #4 add
print(sum,prod," = ",prod-sum)        
