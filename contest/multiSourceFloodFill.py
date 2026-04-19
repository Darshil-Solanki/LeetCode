class Solution:
    def colorGrid(self, n: int, m: int, sources: list[list[int]]) -> list[list[int]]:
        grid = [[0]*m for _ in range(n)]
        overlap_color = [[0]*m for _ in range(n)]
        queue = deque(sources)
        
                
        for r, c, color in sources:
            grid[r][c] = color
            
        while queue:
            curr = set()
            for _ in range(len(queue)):
                r, c, color = queue.popleft()
                if r+1<n and grid[r+1][c]==0:
                    overlap_color[r+1][c] = max(color, overlap_color[r+1][c])
                    curr.add((r+1, c))
                if r-1>-1 and grid[r-1][c]==0:
                    overlap_color[r-1][c] = max(color, overlap_color[r-1][c])
                    curr.add((r-1, c))
                if c-1>-1 and grid[r][c-1]==0:
                    overlap_color[r][c-1] = max(color, overlap_color[r][c-1])
                    curr.add((r, c-1))
                if c+1<m and grid[r][c+1]==0:
                    overlap_color[r][c+1] = max(color, overlap_color[r][c+1])
                    curr.add((r, c+1))
            for r, c in curr:
                grid[r][c] = overlap_color[r][c]
                queue.append((r, c, grid[r][c]))
            
            
        return grid
