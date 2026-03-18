class Solution:
    def countSubmatrices(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        col_sum = [0]*n
        ans = 0

        for i in range(m):
            row_sum = 0
            for j in range(n):
                col_sum[j] += grid[i][j]
                row_sum += col_sum[j]
                if row_sum <= k:
                    ans += 1
        
        return ans
