class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        ans = 0
        min_val = float("inf")
        negative = 0

        for row in matrix:
            for val in row:
                ans += abs(val)
                if val<0:
                    negative +=1
                min_val = min(min_val, abs(val))
        
        if negative%2:
            ans -= 2*min_val
        
        return ans
