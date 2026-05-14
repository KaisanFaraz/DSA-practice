def diff(arr):   #eikhane ekta diff function create korlam                                        #
    max = arr[0]    #max dilam index 0 cz shuru te ami to jani na konta max tai first element e dhorlam max                                                
    min = arr[0]     #min dilam index 0 cz shuru te ami to jani na konta max tai first element e dhorlam min

    for i in range(0,len(arr)):      #loop chalaiman je 0 index theke last index porjonto
        if arr[i]>max:     #jodi arr 0 index max er theke boro hoi taile max e store korba emne sob gula check korbe whole list theke max ber korbe 
            max= arr[i]
        elif arr[i]<min:       #min ber korbe list theke
            min= arr[i]
    return max-min          #diff ber korbe 
arr = list(map(int, input("Enter numbers: ").split())) #list akare 1 2 3 4 emne input newar jonno
result = diff(arr)    #result ekta variable eikhane function er kaaj korbe given input er upor
print("Difference:",result)        #print korbe difference by using the variable result      