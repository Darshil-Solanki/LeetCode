class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        if m==n==1: return grid[0][0]

        def getIndex(k):
            return k//n, k%n

        pathGrid = [[0]*n for i in range(m)]
        for i in range(m):
            pathGrid[i].append(float('inf'))
        pathGrid.append([float('inf')]*n)
        pathGrid[m-1][n-1]=grid[m-1][n-1]
        for k in range(m*n-2,-1,-1):
            i, j = getIndex(k)
            curr = grid[i][j]
            pathGrid[i][j] = min(curr+pathGrid[i+1][j], curr+pathGrid[i][j+1])
        return pathGrid[0][0]
        
        # my first recursive solution
        # m, n = len(grid), len(grid[0])
        # if m==n==1: return grid[0][0]
        # m-=1;n-=1
        # def dp(i, j, pathSum):
        #     curr = grid[i][j]
        #     if i==m and j==n:
        #         return pathSum+curr
        #     a = b = float("inf")
        #     if i+1<=m:
        #         a = dp(i+1, j, pathSum+curr)
        #     if j+1<=n:
        #         b = dp(i, j+1, pathSum+curr)
        #     return min(a, b)
        # return dp(0,0,0)
        
