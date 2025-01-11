from math import comb
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0]*(n+1) for _ in range(m+1)]
        dp[m-1][n-1]=1
        for idx in range(m*n-2, -1, -1):
            i, j = idx//n, idx%n
            dp[i][j]= dp[i+1][j] + dp[i][j+1]
        return dp[0][0]
        
        # One row optimization by chatgpt
        # Initialize a single row for the bottom row of the grid
        # currentRow = [1] * n

        # Iterate from the second-to-last row to the top row
        # for _ in range(m - 1):
        #     for i in range(n - 2, -1, -1):  # Traverse from right to left
        #         currentRow[i] += currentRow[i + 1]  # Add value from the right cell

        # return currentRow[0]

        # mathematical way of doing it using combinations
        # return comb(m+n-2, m-1)

        # using only one variable by chatgpt
        # total = m + n - 2
        # choose = min(m - 1, n - 1)  # Pick the smaller of the two
        # result = 1

        # for i in range(choose):
        #     result = result * (total - i) // (i + 1)
        # return result
