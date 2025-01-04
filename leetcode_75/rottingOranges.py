class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        queue = deque()
        fresh = 0
        for i, row in enumerate(grid):
            for j, cell in enumerate(row):
                if cell==1:
                    fresh+=1
                elif cell==2:
                    queue.append((i,j))
        ans = 0
        while queue:
            if not fresh:
                return ans
            ans +=1
            for _ in range(len(queue)):
                x, y = queue.popleft()
                if x<m-1 and grid[x+1][y]==1:
                    grid[x+1][y]=2
                    queue.append((x+1,y))
                    fresh-=1
                if x>0 and grid[x-1][y]==1:
                    grid[x-1][y]=2
                    queue.append((x-1,y))
                    fresh-=1
                if y<n-1 and grid[x][y+1]==1:
                    grid[x][y+1]=2
                    queue.append((x,y+1))
                    fresh-=1
                if y>0 and grid[x][y-1]==1:
                    grid[x][y-1]=2
                    queue.append((x,y-1))
                    fresh-=1
        return -1 if fresh else ans
