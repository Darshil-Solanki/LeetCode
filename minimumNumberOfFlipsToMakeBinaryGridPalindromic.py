class Solution:
    def minFlips(self, grid: List[List[int]]) -> int:
        row_flips = 0
        col_flips = 0

        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                # count for row
                if j<n//2 and grid[i][j]!=grid[i][n-j-1]:
                    row_flips+=1
                # count for column
                if i<m//2 and grid[i][j]!=grid[m-i-1][j]:
                    col_flips+=1

        return min(row_flips, col_flips)
