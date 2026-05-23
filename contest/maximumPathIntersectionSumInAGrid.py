class Solution:
    def maxScore(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        ans = float("-inf")
        for i in range(1, m - 1):
            for j in range(1, n - 1):
                ans = max(ans, grid[i][j])
        for i in range(m):
            f = grid[i][0]
            for j in range(1, n):
                ans = max(ans, f + grid[i][j])
                f = max(f + grid[i][j], grid[i][j])
        for j in range(n):
            f = grid[0][j]
            for i in range(1, m):
                ans = max(ans, f + grid[i][j])
                f = max(f + grid[i][j], grid[i][j])
        return ans
