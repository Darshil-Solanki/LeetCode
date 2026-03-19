class Solution:
    def numberOfSubmatrices(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        prefix_sum_col = [[0, 0] for _ in range(n)]
        ans = 0

        for i in range(m):
            row_sum = [0, 0]
            for j in range(n):
                if grid[i][j] == "X":
                    prefix_sum_col[j][0] += 1
                elif grid[i][j] == "Y":
                    prefix_sum_col[j][1] += 1
                
                row_sum = [row_sum[0]+prefix_sum_col[j][0], row_sum[1]+prefix_sum_col[j][1]]
                if row_sum[0]>0 and row_sum[0] == row_sum[1]:
                    ans += 1
        
        return ans
