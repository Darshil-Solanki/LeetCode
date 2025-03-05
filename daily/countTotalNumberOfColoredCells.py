class Solution:
    def coloredCells(self, n: int) -> int:
        return 2*n*n-2*n+1
        # ans is based on 1, 5, 13, 25, 41 .... 
        # taken 2 common
        # return 1 + n * (n - 1) * 2
