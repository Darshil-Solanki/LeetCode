class Solution:
    def maxPathScore(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        
        cost_add = {0:0, 1:1, 2:1}
        dp = [[[-1]*(k+1) for _ in range(n)]for _ in range(m)]
        dp[0][0][0] = 0

        for i in range(m):
            for j in range(n):
                for cost_used in range(k+1):
                    if dp[i][j][cost_used] == -1:
                        continue

                    curr_score = dp[i][j][cost_used]

                    if i+1<m:
                        nc = cost_used + cost_add[grid[i+1][j]]
                        if nc <= k:
                            ns = curr_score + grid[i+1][j]
                            dp[i+1][j][nc] = max(dp[i+1][j][nc], ns)

                    if j+1<n:
                        nc = cost_used + cost_add[grid[i][j+1]]
                        if nc<=k:
                            ns = curr_score + grid[i][j+1]
                            dp[i][j+1][nc] = max(dp[i][j+1][nc], ns)
        
        return max(dp[m-1][n-1])
