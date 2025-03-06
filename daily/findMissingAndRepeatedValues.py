class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        table = [0]*(n*n+1)
        repeat = 0

        for i, row in enumerate(grid):
            for j, num in enumerate(row):
                if table[num]:
                    repeat = num
                table[num]=1

        for i in range(1, n*n+1):
            if not table[i]:
                return [repeat, i]
    
    # using math
    # def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
    #     n = len(grid)
    #     table = [0]*(n*n+1)
    #     repeat = 0
    #     totSum = 0

    #     for i, row in enumerate(grid):
    #         for j, num in enumerate(row):
    #             if table[num]:
    #                 repeat = num
    #             table[num]=1
    #             totSum+=num
        
    #     perfSum = n*n*(n*n+1)//2
    #     return [repeat, perfSum+repeat-totSum]
