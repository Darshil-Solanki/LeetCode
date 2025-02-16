class Solution:
    def hasSpecialSubstring(self, s: str, k: int) -> bool:
        i = 0
        while i<len(s):
            curr = s[i]
            i+=1
            tempK = 1
            while i<len(s) and s[i]==curr:
                tempK+=1
                i+=1
            if tempK==k:
                return True
        return False
