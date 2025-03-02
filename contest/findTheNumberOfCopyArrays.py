class Solution:
    def countArrays(self, original: List[int], bounds: List[List[int]]) -> int:
        low, high = bounds[0]
        ans = high-low+1

        for i in range(1, len(original)):
            diff = original[i]-original[i-1]
            low = max(low+diff, bounds[i][0])
            high = min(high+diff, bounds[i][1])
            ans = min(ans, high-low+1)
        
        return 0 if ans<0 else ans
