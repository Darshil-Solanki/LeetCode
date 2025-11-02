class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        # 1 for unguarded
        grid = [[1]*n for _ in range(m)] 

        # 0 for wall
        for w_x, w_y in walls:
            grid[w_x][w_y] = 0
        
        # -1 for guarded, 2 for guard
        for g_x, g_y in guards:
            grid[g_x][g_y] = 2
        
        for g_x, g_y in guards:
            # left
            for i in range(g_y-1, -1, -1):
                if not grid[g_x][i] or grid[g_x][i]==2:
                    break
                grid[g_x][i] = -1
            # right
            for i in range(g_y+1, n):
                if not grid[g_x][i] or grid[g_x][i]==2:
                    break
                grid[g_x][i] = -1
            # top
            for i in range(g_x-1, -1, -1):
                if not grid[i][g_y] or grid[i][g_y]==2:
                    break
                grid[i][g_y] = -1
            # down
            for i in range(g_x+1, m):
                if not grid[i][g_y] or grid[i][g_y]==2:
                    break
                grid[i][g_y] = -1
        
        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:
                    ans += 1
        
        return ans
