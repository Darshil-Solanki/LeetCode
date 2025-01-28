class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        ans = 0
        for i  in range(m):
            for j in range(n):
                if grid[i][j]:
                    curr = 0
                    queue = deque([(i,j)])
                    while queue:
                        x, y = queue.popleft()
                        curr+=grid[x][y]
                        grid[x][y] = 0
                        if (x>0 and grid[x-1][y]): queue.append((x-1,y))
                        if (x < m-1 and grid[x+1][y]): queue.append((x+1,y))
                        if (y>0 and grid[x][y-1]): queue.append((x,y-1))
                        if (y<n-1 and grid[x][y+1]): queue.append((x,y+1))
                    if curr>ans: ans = curr
        return ans

    # More Lower Runtime 
    # def dfs(self, grid, i, j):
    #     nrow, ncol = len(grid), len(grid[0])
    #     if i < 0 or j < 0 or i >= nrow or j >= ncol:
    #         return 0
    #     if grid[i][j] == 0:
    #         return 0
    #     temp = grid[i][j]
    #     grid[i][j] = 0
    #     return temp + self.dfs(grid, i+1, j) + self.dfs(grid, i-1, j) + self.dfs(grid, i, j+1) + self.dfs(grid, i, j-1)

    # def findMaxFish(self, grid: List[List[int]]) -> int:
    #     res = 0
    #     nrow, ncol = len(grid), len(grid[0])
    #     for i in range(nrow):
    #         for j in range(ncol):
    #             if grid[i][j] != 0:
    #                 res = max(res, self.dfs(grid, i, j))
    #     return res
