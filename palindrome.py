n=int(input("Enter number: "))
temp = n
rev = 0
while temp >0:
    r = temp%10
    temp //=10
    rev= rev*10 + r

if n == rev:
    print("Palindrome")
else:
    print("Not Palindrome")        
  