class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        l=s.split()
        return len(l[-1])
        
# Copied from discussion
# class Solution:
#     def lengthOfLastWord(self, s):
#         end = len(s) - 1
#         while end > 0 and s[end] == " ": end -= 1
#         beg = end
#         while beg >= 0 and s[beg] != " ": beg -= 1
#         return end - beg
        
