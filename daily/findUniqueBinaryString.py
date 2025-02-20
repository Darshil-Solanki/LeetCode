class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n = len(nums)
        numSet = set(nums)

        def backtrack(i, curr):
            if i==n:
                if curr not in numSet: return curr
                return ""
            
            for j in range(2):
                res = backtrack(i+1, curr+str(j))
                if res: return res
        
        return backtrack(0, "")
