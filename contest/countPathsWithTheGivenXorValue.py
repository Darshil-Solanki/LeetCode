class Solution:
    def countPathsWithXorValue(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        count = 0
        direction = [(0,1),(1,0)]
        def backtrack(i, j, pathSum):
            nonlocal count
            if (i, j) == (m-1, n-1):
                if pathSum==k:
                    count+=1
            for dx,dy in direction:
                cx, cy = i+dx, j+dy
                if -1<cx<m and -1<cy<n:
                    temp = pathSum
                    temp ^= grid[cx][cy]
                    backtrack(cx, cy, temp)
        backtrack(0,0,grid[0][0])
        return count%1000_000_007

# Copied from contest top submission
# MOD = 10**9+7
# class Solution:
#     def countPathsWithXorValue(self, grid: List[List[int]], tar: int) -> int:
#         m, n = len(grid), len(grid[0])
#         dp = [[[0] * 16 for _ in range(n+1)] for _ in range(m+1)]
#         dp[0][1][0] = 1
#         for i, row in enumerate(grid):
#             for j, x in enumerate(row):
#                 for k in range(16):
#                     dp[i+1][j+1][k] = (dp[i][j+1][k^x] + dp[i+1][j][k^x]) % MOD
#         return dp[m][n][tar]
