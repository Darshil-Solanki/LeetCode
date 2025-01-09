class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        result = []
        
        def backtrack(curr, tot, length, ans):
            if length==k:
                if tot==n:
                    result.append(ans[:])
                return
            for i in range(curr+1, 10):
                ans.append(i)
                backtrack(i, tot+i, length+1, ans)
                ans.pop()

        backtrack(0, 0, 0, [])
        return result
