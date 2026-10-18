class Solution:
    def lastVisitedCell(self, grid: list[list[str]]) -> list[int]:
        m, n = len(grid), len(grid[0])
        visited = [[False]*n for _ in range(m)]

        def visit(i, j):
            next_move = grid[i][j]
            visited[i][j] = True
            dx, dy = 0, 0
            if next_move == "L":
                dx, dy = 0, -1
            elif next_move == "R":
                dx, dy = 0, 1
            elif next_move == "U":
                dx, dy = -1, 0
            else:
                dx, dy = 1, 0

            ni, nj = i+dx, j+dy
            if ni<0 or ni==m or nj<0 or nj==n or visited[ni][nj]:
                return [i, j]

            return visit(ni, nj)

        return visit(0, 0)
