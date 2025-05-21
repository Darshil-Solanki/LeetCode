class Solution:
    def countPathsWithXorValue(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        MOD = 1_000_000_007
        count = 0

        @cache
        def dp(i, j):
            if i<0 or j<0: return Counter()
            if (i, j) == (0,0): return Counter({grid[0][0]:1})
            prev = dp(i-1, j) + dp(i, j-1)
            return Counter({v ^ grid[i][j]: prev[v]%MOD for v in prev})
        
        counts = dp(m-1, n-1)
        return counts[k]%MOD 
