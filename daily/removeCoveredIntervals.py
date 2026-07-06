class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x: (x[0], -x[1]))
        ans = n = len(intervals)
        low, high = intervals[0]

        for i in range(1, n):
            curr_l, curr_h = intervals[i]
            if curr_l == low or curr_h <= high:
                ans -= 1
            else:
                low, high = curr_l, curr_h
        
        return ans
