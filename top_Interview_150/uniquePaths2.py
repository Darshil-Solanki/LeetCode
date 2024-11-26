class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        if obstacleGrid[m-1][n-1]: return 0
        if m==n==1: return 1
        def getIndex(k):
            return k//n, k%n
        pathGrid = [[0]*n for i in range(m)]
        for i in range(m):
            pathGrid[i].append(0)
        pathGrid.append([0]*n)
        pathGrid[m-1][n-1]=1
        for k in range(m*n-2, -1, -1):
            i, j = getIndex(k)
            curr = obstacleGrid[i][j]
            if not curr:
                pathGrid[i][j] = pathGrid[i+1][j]+pathGrid[i][j+1]
        return pathGrid[0][0]
