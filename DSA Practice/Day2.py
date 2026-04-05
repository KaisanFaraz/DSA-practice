''' 
n = 100
while n>0:
    print(n,end=" ")
    n//=2
''' 
'''
n = 1
while n<=100:
    print(n,end=" ")
    n*=2
 '''
'''
def printnumbers(i,n):
    if i>n:
        return
   
    print(i,end=" ")
    printnumbers(i+1,n)
printnumbers(1,5)    
'''
'''
def fact(n):
 if n == 0:
  return 1
 return n*fact(n-1)

print(fact(4))
'''
'''
def fun(n):
    if n==0:
        return
    fun(n-1)
    print(n,end=" ")
   # fun(n-1)
fun(3)    
'''
n = int(input())
while n%2 ==0:
    n//=2
    if n==1:
        print("t")
    else:
        print("F")    