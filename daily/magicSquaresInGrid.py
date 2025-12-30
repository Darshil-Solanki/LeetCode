class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        if len(grid)<3: return 0
        ans = 0
        m, n = len(grid), len(grid[0])

        def check_magick_square(i, j):
            if i==0 or j==0 or i==m-1 or j==n-1:
                return False
            row_sum = [sum(grid[i-1][j-1:j+2])!=15, sum(grid[i][j-1:j+2])!=15, sum(grid[i+1][j-1:j+2])!=15]
            if any(row_sum): return False
            col_sum = [
                (grid[i][j-1] + grid[i-1][j-1] + grid[i+1][j-1])!=15,
                (grid[i][j] + grid[i-1][j] + grid[i+1][j])!=15,
                (grid[i][j+1] + grid[i-1][j+1] + grid[i+1][j+1])!=15
            ]
            if any(col_sum): return False
            di_sum = [
                (grid[i-1][j-1]+grid[i][j]+grid[i+1][j+1])!=15,
                (grid[i-1][j+1]+grid[i][j]+grid[i+1][j-1])!=15
            ]
            if any(di_sum): return False
            nums = grid[i-1][j-1:j+2] + grid[i][j-1:j+2] + grid[i+1][j-1:j+2]
            return all(i in nums for i in range(1, 10))

        for i, row in enumerate(grid):
            for j, num in enumerate(row):
                if num==5 and check_magick_square(i, j):
                    ans += 1

        return ans
