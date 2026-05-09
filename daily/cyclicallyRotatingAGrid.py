class Solution:
    def rotateGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        layer = min(m//2, n//2)

        for ly in range(layer):
            val = []
            r, c = [], []
            for i in range(ly, m-ly-1): # left
                r.append(i)
                c.append(ly)
                val.append(grid[i][ly])
            for j in range(ly, n-ly-1): # bottom
                r.append(m-ly-1)
                c.append(j)
                val.append(grid[m-ly-1][j])
            for i in range(m-ly-1, ly, -1): # right
                r.append(i)
                c.append(n-ly-1)
                val.append(grid[i][n-ly-1])
            for j in range(n-ly-1, ly, -1): # top
                r.append(ly)
                c.append(j)
                val.append(grid[ly][j])
            
            total = len(val)
            reduce_k = k % total
            for i in range(total):
                new_i = (i+total-reduce_k) % total
                grid[r[i]][c[i]] = val[new_i]
        return grid
