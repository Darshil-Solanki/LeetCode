class Solution:
    def uniquePaths(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        MOD = 1_000_000_007
        dp = [[[0, 0] for _ in range(n)] for _ in range(m)]

        # Base case: Initialize first row
        for j in range(len(grid[0])):
            dp[0][j] = [1, 0]
            if grid[0][j] == 1:
                break
        
        # Base case: Initialize first column
        for i in range(len(grid)):
            dp[i][0] = [0, 1]
            if grid[i][0] == 1:
                break

        # Fill the rest of the DP table
        for i in range(1, len(grid)):
            for j in range(1, len(grid[0])):
                # Paths from above
                if grid[i-1][j] == 1:
                    dp[i][j][1] = dp[i-1][j][0]
                else:
                    dp[i][j][1] = dp[i-1][j][0] + dp[i-1][j][1]

                # Paths from left
                if grid[i][j-1] == 1:
                    dp[i][j][0] = dp[i][j-1][1]
                else:
                    dp[i][j][0] = dp[i][j-1][0] + dp[i][j-1][1]
        return sum(dp[-1][-1]) % MOD
