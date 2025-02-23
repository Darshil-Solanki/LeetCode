class Solution:
    def hasSameDigits(self, s: str) -> bool:
        while len(s)>2:
            value = ""
            for i in range(1, len(s)):
                value+=str((int(s[i-1])+int(s[i]))%10)
            s = value
        return s[0]==s[1]
