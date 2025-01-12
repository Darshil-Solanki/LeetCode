class Solution:
    def zigzagTraversal(self, grid: List[List[int]]) -> List[int]:
        res = []
        m, n  = len(grid), len(grid[0])
        flag = True
        i = j = 0 
        while i<m:
            while (j<n if flag else j>-1):
                res.append(grid[i][j])
                j = j+2 if flag else j-2
            if flag:
                j = n-1 if j==n else n-2
            else:
                j = 0 if j<0 else 1                
            flag = not flag
            i+=1
        return res

        # from top player in contest
        # ans = []
        # f = 1
        # for v in grid:
        #     if f: ans.extend(v)
        #     else: ans.extend(v[::-1])
        #     f ^= 1
        # return ans[::2]
