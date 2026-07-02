class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        m, n = len(grid), len(grid[0])
        min_cost = [[-1]*n for _ in range(m)]
        dirs = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        queue = [(grid[0][0], 0, 0)]
        
        while queue:
            cost, i, j = heappop(queue)
            if min_cost[i][j]>=0:
                continue
            min_cost[i][j] = cost
            for dx, dy in dirs:
                nx, ny = dx+i, dy+j
                if -1<nx<m and -1<ny<n and min_cost[nx][ny]==-1:
                    heappush(queue, (cost+grid[nx][ny], nx, ny))
        
        return min_cost[m-1][n-1]<health
