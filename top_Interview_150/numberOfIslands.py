class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        rows, cols = len(grid), len(grid[0])
        self.grid = grid
        def dfs(r,c):
            self.grid[r][c]="O"
            if r<rows-1 and self.grid[r+1][c]=="1":
                dfs(r+1,c)
            if r>0 and self.grid[r-1][c]=="1":
                dfs(r-1,c)
            if c<cols-1 and self.grid[r][c+1]=="1":
                dfs(r,c+1)
            if c>0 and self.grid[r][c-1]=="1":
                dfs(r,c-1)

        res = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]=="1":
                    dfs(r,c)
                    res+=1
        return res
    # BFS way
    # def numIslands(self, grid: List[List[str]]) -> int:
    #     if not grid:
    #         return 0
    #     ans = 0
    #     seen = set()
    #     def bfs(r,c):
    #         queue = [(r,c)]
    #         seen.add((r,c))
    #         while queue:
    #             cr, cc = queue.pop(0)
    #             direction = [[1,0], [-1,0], [0, 1], [0, -1]]
    #             for dr, dc in direction:
    #                 r, c = cr+dr, cc+dc
    #                 if (r in range(rows) and 
    #                 c in range(cols)  and 
    #                 grid[r][c] == "1" and 
    #                 (r, c) not in seen):
    #                     queue.append((r,c))
    #                     seen.add((r,c))


    #     rows, cols = len(grid), len(grid[0])
    #     for r in range(rows):
    #         for c in range(cols):
    #             if grid[r][c]=="1" and (r, c) not in seen:
    #                 bfs(r,c)
    #                 ans+= 1
    #     return ans
