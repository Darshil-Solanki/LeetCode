class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        li=0
        for i in range(len(s)):
            flag = False
            for j in range(li, len(t)):
                if s[i]==t[j]:
                    li=j+1
                    flag=True
                    break
            if not flag:
                return False
        return True

# Better Solution
# class Solution:
#     def isSubsequence(self, s:str, t:str)-> bool:
#         sp = tp = 0
#         while sp<len(s) and tp<len(t):
#             if s[sp]==t[tp]:
#                 sp+=1
#             tp+=1
#         return sp==len(s)

# class Solution:
#     def isSubsequence(self, s: str, t: str) -> bool:
#         k='' 
#         j=0
#         if s==''  :
#             return True
#         for  i in t:
#             if i ==s[j]:
#                 k+=i
#                 if len(s)-1>j:
#                     j+=1
#         return k==s
