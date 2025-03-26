class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        values = []
        remainders = {}
        for i, row in enumerate(grid):
            for j, val in enumerate(row):
                remainders[val%x]=1
                values.append(val)
        
        if len(remainders)>1: return -1
        values.sort()
        
        mid = (len(values)-1)//2
        midVal = values[mid]
        ans = 0
        for val in values:
            if val!=midVal:
                ans+=abs(midVal-val)//x
        
        return ans
