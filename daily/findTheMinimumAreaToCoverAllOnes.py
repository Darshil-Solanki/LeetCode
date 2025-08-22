class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        lw, rw, th, bh =  n, -1, m, 0
        
        for i, row in enumerate(grid):
            for j, val in enumerate(row):
                if val:
                    th, bh = min(th, i), i
                    lw, rw = min(lw, j), max(rw, j)
        
        return (rw-lw+1)*(bh-th+1)
