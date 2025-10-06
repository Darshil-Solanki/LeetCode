class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        visited = [[False]*n for _ in range(n)]
        heap = [(grid[0][0], 0, 0)]
        visited[0][0] = True
        ans = 0

        while heap:
            t, i, j = heappop(heap)
            ans = max(ans, t)
            if i == j == n-1:
                return ans
            
            if i+1<n and not visited[i+1][j]:
                visited[i+1][j] = True
                heappush(heap, (grid[i+1][j], i+1, j))

            if i-1>-1 and not visited[i-1][j]:
                visited[i-1][j] = True
                heappush(heap, (grid[i-1][j], i-1, j))
            
            if j+1<n and not visited[i][j+1]:
                visited[i][j+1] = True
                heappush(heap, (grid[i][j+1], i, j+1))
            
            if j-1>-1 and not visited[i][j-1]:
                visited[i][j-1] = True
                heappush(heap, (grid[i][j-1], i, j-1))
