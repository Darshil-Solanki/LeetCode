class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        m, n = len(grid), len(grid[0])

        def is_cycle(i, j):
            def dfs(i, j, pi, pj, c, dist):
                if visited[i][j]:
                    if dist>3:
                        return True
                    return False
                visited[i][j] = True
                
                if i<m-1 and grid[i+1][j]==c and (i+1, j)!=(pi, pj):
                    if dfs(i+1, j, i, j, c, dist+1):
                        return True
                if i>0 and grid[i-1][j]==c and (i-1, j)!=(pi, pj):
                    if dfs(i-1, j, i, j, c, dist+1):
                        return True
                if j>0 and grid[i][j-1]==c and (i, j-1)!=(pi, pj):
                    if dfs(i, j-1, i, j, c, dist+1):
                        return True
                if j<n-1 and grid[i][j+1]==c and (i, j+1)!=(pi, pj):
                    if dfs(i, j+1, i, j, c, dist+1):
                        return True
                return False
            return dfs(i, j, i, j, grid[i][j], 0)

        
        visited = [[0]*n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if not visited[i][j] and is_cycle(i, j):
                    return True
        return False
