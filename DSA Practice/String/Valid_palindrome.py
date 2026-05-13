def Alphanumerical(char):
    x = ord(char)
    if (97<=x<=122) or (65<=x<=90) or (48<=x<=57):
        return True
    return False
def isPalindrome(s):
    s=s.lower()
    i=0
    j=len(s)-1   
    while i<j:
        if not Alphanumerical(s[i]):
            i+=1
        elif not Alphanumerical(s[j]):
            j-=1
        else:
            if s[i] == s[j]:
                i+=1
                j-=1
            else:
                return False
    return True

user_inp = input("Enter String: ")
if isPalindrome(user_inp):
   print("Palindrome")
    
         
else:
  print("Not Palindrome")   



