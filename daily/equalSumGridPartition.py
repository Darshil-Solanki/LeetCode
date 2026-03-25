class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        half_sum, md = divmod(sum(chain(*grid)), 2)
        if md:
            return False

        temp = 0
        for row in grid:
            temp += sum(row)
            if temp==half_sum:
                return True
            if temp>half_sum:
                break
                    
        temp = 0
        for col in zip(*grid):
            temp += sum(col)
            if temp == half_sum:
                return True
            if temp>half_sum:
                return False
        return False
