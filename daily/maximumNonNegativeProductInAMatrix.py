class Solution:
    def maxProductPath(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        MOD = 1_000_000_007

        @cache
        def dp(i, j):
            val = grid[i][j]
            if i==m-1 and j==n-1:
                return (val, val)
            
            candidates = []
            if i+1<m:
                cmax, cmin = dp(i+1, j)
                candidates += [cmax*val, cmin*val]
            if j+1<n:
                cmax, cmin = dp(i, j+1)
                candidates += [cmax*val, cmin*val]
            return (max(candidates), min(candidates))
                    
        ans, _ = dp(0, 0)
        return -1 if ans<0 else ans%MOD
