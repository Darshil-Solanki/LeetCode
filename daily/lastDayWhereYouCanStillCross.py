class Solution:
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:    
        
        def check(day):
            if day==0: return True
            grid = [[0]*col for _ in range(row)]
            for i in range(day):
                r, c = cells[i]
                grid[r-1][c-1] = 1

            seen = [[False]*col for _ in range(row)]
            def dfs(i, j):
                if seen[i][j]:
                    return False
                seen[i][j] = True
                if grid[i][j]:
                    return False
                if i == row-1: return True

                left = right = top = bottom = False
                if j>0:
                    left = dfs(i, j-1)
                if j<col-1:
                    right = dfs(i, j+1)
                if i>0:
                    top = dfs(i-1, j)
                if i<row-1:
                    bottom = dfs(i+1, j)
                return left or right or top or bottom

            for j in range(col):
                if dfs(0, j):
                    return True
            
            return False

        left, right = 0, len(cells)
        ans = 0
        while left<=right:
            mid = (left+right)//2
            if check(mid):
                left = mid+1
                ans = mid
            else:
                right = mid-1
        
        return ans
