import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        x=re.sub(r"[^a-zA-Z0-9]", "", s).lower()
        #x.lower()
        print(x)
        i=0
        j=len(x)-1
        while i<=j:
            print(x[i],x[j])
            if x[i]!=x[j]:
                return False
            i+=1
            j-=1
        return True