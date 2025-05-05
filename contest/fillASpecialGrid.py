class Solution:
    def specialGrid(self, N: int) -> List[List[int]]:
        n = m = 1<<N #2^N
        self.val = 0
        self.grid = [ [0]*n for _ in range(m) ]

        def generate(row_start, row_end, col_start, col_end):
            if row_end - row_start == 1:
                self.grid[row_start][col_start] = self.val
                self.val += 1
                return
            
            mid_row = (row_start + row_end)//2
            mid_col = (col_start + col_end)//2

            # Top-right
            generate(row_start, mid_row, mid_col, col_end)
            # Bottom-right
            generate(mid_row, row_end, mid_col, col_end)
            # Bottom-left
            generate(mid_row, row_end, col_start, mid_col)
            # Top-left
            generate(row_start, mid_row, col_start, mid_col)

        generate(0, m, 0, n)
        return self.grid

    # def specialGrid(self, n: int) -> List[List[int]]:
    #     size = 1
    #     grid = [[0]]

    #     for _ in range(n):
    #         new_size = size * 2
    #         offset = size * size
    #         new_grid = [[0] * new_size for _ in range(new_size)]

    #         for i in range(size):
    #             for j in range(size):
    #                 val = grid[i][j]
    #                 # Top-left: add 3 * offset
    #                 new_grid[i][j] = val + 3 * offset
    #                 # Top-right: add 0 * offset (no change)
    #                 new_grid[i][j + size] = val
    #                 # Bottom-right: add 1 * offset
    #                 new_grid[i + size][j + size] = val + offset
    #                 # Bottom-left: add 2 * offset
    #                 new_grid[i + size][j] = val + 2 * offset

    #         grid = new_grid
    #         size = new_size

    #     return grid
