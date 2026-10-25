class Solution:
    def closedIsland(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])

        def mark(i, j):
            grid[i][j] = -1
            if i>0 and grid[i-1][j] == 0:
                mark(i-1, j)
            if i<m-1 and grid[i+1][j] == 0:
                mark(i+1, j)
            if j>0 and grid[i][j-1] == 0:
                mark(i, j-1)
            if j<n-1 and grid[i][j+1] == 0:
                mark(i, j+1)

        for j in range(n):
            if grid[0][j] == 0:
                mark(0, j)

            if grid[m-1][j] == 0:
                mark(m-1, j)
        
        for i in range(m):
            if grid[i][0] == 0:
                mark(i, 0)
            
            if grid[i][n-1] == 0:
                mark(i, n-1)

        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    mark(i, j)
                    ans += 1
        
        return ans
