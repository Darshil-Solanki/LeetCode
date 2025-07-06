class Solution:
    def minCost(self, m: int, n: int, waitCost: List[List[int]]) -> int:
        @cache
        def dfs(i, j, t):
            if i == m-1 and j == n-1:
                return 0
            if i == m or j == n: 
                return float("inf")
            right = (waitCost[i][j] if t%2==0 else 0) + dfs(i, j+1, (t if t%2==0 else int(not t))) + (i+1)*(j+2)
            down = (waitCost[i][j] if t%2==0 else 0) + dfs(i+1, j, (t if t%2==0 else int(not t))) + (i+2)*(j+1)
            
            return min(right, down)
            
        return 1+dfs(0, 0, 1)
