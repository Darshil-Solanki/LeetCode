class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        dp = [[0]*n for _ in range(n+1)]

        for i in range(1, n+1):
            for j in range(n):
                first, second, third = (dp[i-1][j-1] if j>0 else float("inf")), dp[i-1][j], (dp[i-1][j+1] if j<n-1 else float("inf"))
                dp[i][j] = min(first, second, third)+matrix[i-1][j]
        return min(dp[i])


        # space optimize way
        # n = len(matrix)
        
        # prev_row = matrix[-1][:]

        # for i in range(n-2, -1, -1):
        #     curr_row = [0] * n
        #     for j in range(n):
        #         down = prev_row[j]
        #         diagl = prev_row[j-1] if j>=1 else float('inf')
        #         diagr = prev_row[j+1] if j<=n-2 else float('inf')

        #         curr_row[j] = matrix[i][j] + min(down, diagl, diagr)
        #     prev_row = curr_row
        
        # return min(prev_row)
