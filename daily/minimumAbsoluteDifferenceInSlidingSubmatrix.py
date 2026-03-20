class Solution:
    def minAbsDiff(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        ans = [[0]*(n-k+1) for i in range(m-k+1)]

        for i in range(m-k+1):
            for j in range(n-k+1):
                kgrid = []
                for x in range(i, i+k):
                    for y in range(j, j+k):
                        kgrid.append(grid[x][y])
                curr_min = float("inf")
                kgrid.sort()
                for l in range(1, len(kgrid)):
                    if kgrid[l]==kgrid[l-1]:
                        continue
                    curr_min = min(curr_min, kgrid[l]-kgrid[l-1])
                if curr_min!=float("inf"):
                    ans[i][j] = curr_min
        return ans
