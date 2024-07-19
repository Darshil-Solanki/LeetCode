class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        temp=""
        for i in s:
            if 96<ord(i)<123 or 47<ord(i)<58:
                temp+=i
        if temp=="":
            return True
        n=len(temp)
        return temp[:n//2]==temp[-1:-(n//2)-1:-1]

# class Solution:
#     def isPalindrome(self, s: str) -> bool:
#         s1=s.lower()
#         s2=''.join(char for char in s1 if char.isalnum())
#         return s2==s2[::-1] 
