class RhombusCalculator:
    def __init__(self):
        self.ans = [0, 0, 0]

    def put(self, x):
        if x>self.ans[0]:
            self.ans[0], self.ans[1], self.ans[2] = x, self.ans[0], self.ans[1]
        elif x!=self.ans[0] and x>self.ans[1]:
            self.ans[1], self.ans[2] = x, self.ans[1]
        elif x!=self.ans[0] and x!=self.ans[1] and x>self.ans[2]:
            self.ans[2] = x

    def get(self):
        return [num for num in self.ans if num!=0]

class Solution:
    def getBiggestThree(self, grid: List[List[int]]) -> List[int]:
        m, n = len(grid), len(grid[0])
        sum1 = [[0]*(n+2) for _ in range(m+1)]
        sum2 = [[0]*(n+2) for _ in range(m+1)]
        
        for i in range(1, m+1):
            for j in range(1, n+1):
                sum1[i][j] = sum1[i-1][j-1] + grid[i-1][j-1]
                sum2[i][j] = sum2[i-1][j+1] + grid[i-1][j-1]
        
        rbs = RhombusCalculator()
        for i in range(m):
            for j in range(n):
                rbs.put(grid[i][j]) # single cell rhombus
                for k in range(i+2, m, 2):
                    ux, uy = i, j
                    dx, dy = k, j
                    lx, ly = (i+k)//2, j-(k-i)//2
                    rx, ry = (i+k)//2, j+(k-i)//2
                    if ly<0 or ry>=n:
                        break
                    
                    rbs.put(
                        (sum2[lx + 1][ly + 1] - sum2[ux][uy + 2])
                        + (sum1[rx + 1][ry + 1] - sum1[ux][uy])
                        + (sum1[dx + 1][dy + 1] - sum1[lx][ly])
                        + (sum2[dx + 1][dy + 1] - sum2[rx][ry + 2])
                        - (
                            grid[ux][uy]
                            + grid[dx][dy]
                            + grid[lx][ly]
                            + grid[rx][ry]
                        )
                    )
        return rbs.get()
