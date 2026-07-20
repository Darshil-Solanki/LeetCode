class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        if not k:
            return grid
        m, n = len(grid), len(grid[0])
        total = m * n
        k = k % total

        def get_new_idx(i, j):
            old_idx = i * n + j
            new_idx = (old_idx + k) % total
            return new_idx // n, new_idx % n

        new_grid = [[0] * n for _ in range(m)]
        for i, row in enumerate(grid):
            for j, num in enumerate(row):
                ni, nj = get_new_idx(i, j)
                new_grid[ni][nj] = num
        
        return new_grid
