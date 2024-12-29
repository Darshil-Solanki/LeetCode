class Solution:
    def minimumOperations(self, grid: List[List[int]]) -> int:
        count=[0]*len(grid[0])
        for i in range(len(grid[0])):
            prev = 0
            for j in range(len(grid)):
                if j and grid[j][i]<=prev:
                    count[i]+=(prev-grid[j][i]+1)
                    prev += 1
                else:
                    prev = grid[j][i]
        return sum(count)
