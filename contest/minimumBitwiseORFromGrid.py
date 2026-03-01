class Solution:
    def minimumOR(self, grid: List[List[int]]) -> int:
        # copied from solution
        m = len(grid)

        # Values <= 1e5 => need up to 17 bits. Using 20 bits safely.
        MAXB = 20
        M = (1 << MAXB) - 1  # start with all bits allowed

        def feasible(mask: int) -> bool:
            for row in grid:
                ok = False
                for x in row:
                    # Check if x is a subset of mask
                    if (x & ~mask) == 0:
                        ok = True
                        break
                if not ok:
                    return False  # this row has no valid pick
            return True

        # Try removing bits from high to low
        for b in range(MAXB - 1, -1, -1):
            M2 = M & ~(1 << b)
            if feasible(M2):
                M = M2

        return M

        # my contest solution TLE
        # m, n = len(grid), len(grid[0])
        # for i in range(m):
        #     grid[i].sort()
        
        # @lru_cache
        # def dp(row, curr_ans):
        #     if row==m: return curr_ans
        #     ans = float("inf")
        #     for j in range(n):
        #         ans = min(ans, dp(row+1, curr_ans|grid[row][j]))
        #     return ans
        
        # return dp(0, 0)
