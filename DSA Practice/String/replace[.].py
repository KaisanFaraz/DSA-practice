class Solution:
    def defangIPaddr(self, address: str) -> str:    #1.1.1.1   1[.]1[.]1[.]1
        ans = ""                                     ans = "1[.]"   
        for i in address:                             i =  . 
            if  i != ".":                             1 = 1+[.]   1[.]
                ans = ans+i
            else:
                ans =ans+"[.]"

        return ans 