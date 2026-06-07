class Solution:
    def generateValidStrings(self, n: int, k: int) -> list[str]:
        ans = []
        def backtrack(curr, i, limit):
            if len(curr)==n:
                ans.append("".join(curr))
                return
            
            if limit-i>-1:
                if i>0:
                    if curr[-1]=="0":
                        backtrack(curr+["1"], i+1, limit-i)
                else:
                    backtrack(curr+["1"], i+1, limit-i)
                    
            curr.append("0")
            backtrack(curr, i+1, limit)

        backtrack([], 0, k)
        return ans
