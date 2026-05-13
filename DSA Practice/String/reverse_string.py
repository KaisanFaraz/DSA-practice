def isreverse(s):
    container=s.split()
    i = 0
    j =len(container)-1
    while i<j:
        temp = container[i]
        container[i] = container[j]
        container[j]=temp
        i+=1
        j-=1
    return " ".join(container)    
u_input = input("Enter String: ")
result = isreverse(u_input)
print("Reversed: ",result)
         

        
        




