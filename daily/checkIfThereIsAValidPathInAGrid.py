class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        m, n = len(grid), len(grid[0])

        def dfs(i, j):
            if i == 0 and j == 0:
                return True
            
            path = grid[i][j]
            visited[i][j] = True
            ans = False
            match path:
                case 1:
                    move1 = dfs(i, j-1) if j>0 and not visited[i][j-1] and grid[i][j-1] in (1, 4, 6) else False
                    move2 = dfs(i, j+1) if j<n-1 and not visited[i][j+1] and grid[i][j+1] in (1, 3, 5) else False
                case 2:
                    move1 = dfs(i-1, j) if i>0 and not visited[i-1][j] and grid[i-1][j] in (3, 4, 2) else False
                    move2 = dfs(i+1, j) if i<m-1 and not visited[i+1][j] and grid[i+1][j] in (5, 6, 2) else False
                case 3:
                    move1 = dfs(i, j-1) if j>0 and not visited[i][j-1] and grid[i][j-1] in (1, 4, 6) else False
                    move2 = dfs(i+1, j) if i<m-1 and not visited[i+1][j] and grid[i+1][j] in (2, 5, 6) else False
                case 4:
                    move1 = dfs(i, j+1) if j<n-1 and not visited[i][j+1] and grid[i][j+1] in (1, 3, 5) else False
                    move2 = dfs(i+1, j) if i<m-1 and not visited[i+1][j] and grid[i+1][j] in (2, 5, 6) else False
                case 5:
                    move1 = dfs(i-1, j) if i>0 and not visited[i-1][j] and grid[i-1][j] in (3, 4, 2) else False
                    move2 = dfs(i, j-1) if j>0 and not visited[i][j-1] and grid[i][j-1] in (1, 4, 6) else False
                case 6:
                    move1 = dfs(i-1, j) if i>0 and not visited[i-1][j] and grid[i-1][j] in (3, 4, 2) else False
                    move2 = dfs(i, j+1) if j<n-1 and not visited[i][j+1] and grid[i][j+1] in (1, 3, 5) else False
            return move1 | move2

        visited = [[False]*n for _ in range(m)]
        return dfs(m-1, n-1)
