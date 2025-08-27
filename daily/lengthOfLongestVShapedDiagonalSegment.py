class Solution:
    def lenOfVDiagonal(self, grid: List[List[int]]) -> int:
        directions = [(1, 1), (1, -1), (-1, -1), (-1, 1)]
        m, n = len(grid), len(grid[0])

        @functools.cache
        def dfs(cx, cy, direction, turn, target):
            nx, ny = cx+directions[direction][0], cy+directions[direction][1]

            if nx<0 or ny<0 or nx>=m or ny>=n or grid[nx][ny]!=target:
                return 0
            
            max_step = dfs(nx, ny, direction, turn, 2-target)
            if turn:
                max_step = max(max_step, dfs(nx, ny, (direction+1)%4, False, 2-target))
            
            return max_step+1
        
        ans = 0
        for i, row in enumerate(grid):
            for j, val in enumerate(row):
                if val == 1:
                    for direction in range(4):
                            ans = max(ans, dfs(i, j, direction, True, 2)+1)

        return ans
