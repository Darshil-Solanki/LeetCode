class Solution:
    def hasValidPath(self, grid: list[list[str]]) -> bool:
        m, n = len(grid), len(grid[0])
        path_len = m + n - 1

        if path_len % 2 or grid[0][0] != "(" or grid[-1][-1] != ")":
            return False
        
        prev, curr = [0]*n, [0]*n
        prev[0] = 1 << 1

        for i in range(m):
            curr = [0]*n
            if i==0:
                curr[0] = 1 << 1
            for j in range(n):
                change = 1 if grid[i][j] == "(" else -1
                if i > 0:
                    if change == 1:
                        curr[j] |= prev[j] << 1
                    else:
                        curr[j] |= prev[j] >> 1
                if j > 0:
                    if change == 1:
                        curr[j] |= curr[j-1] << 1
                    else:
                        curr[j] |= curr[j-1] >> 1
            
            prev = curr
            
        
        return bool(curr[-1] & 1)
