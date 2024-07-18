class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        temp=strs[0]
        ans=""
        for i in temp:
            for j in strs:
                if not j.startswith(ans+i):
                    return ans
            else:
                ans+=i
        return ans
                
# class Solution:
#     def longestCommonPrefix(self, strs: List[str]) -> str:
#         ans=""
#         list=sorted(strs)
#         first=list[0]
#         last=list[-1]

#         for i in range(min(len(first),len(last))):
#             if(first[i]!=last[i]):
#                 return ans
#             ans+=first[i]
#         return ans
                
            
