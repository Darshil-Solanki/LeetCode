class Solution:
    def countIslands(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        
        def dfs(i, j):
            if not grid[i][j]: return 0
            ans = grid[i][j]
            if i>0 and (i-1, j) not in seen: #top
                seen.add((i-1, j))
                ans += dfs(i-1, j)
            if i<m-1 and (i+1, j) not in seen: #down
                seen.add((i+1, j))
                ans += dfs(i+1, j)
            if j>0 and (i, j-1) not in seen: #left
                seen.add((i, j-1))
                ans += dfs(i, j-1)
            if j<n-1 and (i, j+1) not in seen: #right
                seen.add((i, j+1))
                ans += dfs(i, j+1)
            return ans
            
        seen = set()
        count = 0
        for i, row in enumerate(grid):
            for j, num in enumerate(row):
                if (i, j) not in seen:
                    seen.add((i,j))
                    if num:
                        if dfs(i, j)%k==0:
                            count += 1

        return count
