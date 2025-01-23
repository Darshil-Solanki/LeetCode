class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        rowCount, colCount = [0]*len(grid), [0]*len(grid[0])
        for i, row in enumerate(grid):
            for j, cell in enumerate(row):
                if cell:
                    rowCount[i]+=1
                    colCount[j]+=1
        ans = 0
        for i, row in enumerate(grid):
            for j, cell in enumerate(row):
                if cell:
                    if rowCount[i]>1 or colCount[j]>1:
                        ans+=1
        return ans

        # faster method counting all row element and only necessary column server in n instead of 2n time complexity
        # count = 0
        # for r in range(len(grid)):
        #     s = sum(grid[r])
        #     if s > 1:
        #         count += s
        #     elif s == 1:
        #         column = grid[r].index(1)
        #         if sum(grid[r][column] for r in range(len(grid))) > 1:
        #             count += 1
        # return count
