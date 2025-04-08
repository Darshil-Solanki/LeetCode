class Solution:
    def countArrays(self, original: List[int], bounds: List[List[int]]) -> int:
        left, right = bounds[0]

        for i in range(1, len(original)):
            delta = original[i]-original[i-1]

            left = max(bounds[i][0], left+delta)
            right = min(bounds[i][1], right+delta)
        
            if left>right: return 0
        
        return right-left+1
