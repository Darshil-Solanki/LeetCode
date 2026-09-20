class Solution:
    def countIntersectingIntervals(self, intervals: list[list[int]]) -> int:
        intervals.sort()
        def bisearch(end):
            left, right = 0, len(intervals)
            while left<right:
                mid = (left+right)//2
                if end<intervals[mid][0]:
                    right = mid
                else:
                    left = mid + 1
            return left

        ans = 0
        for i, (s, e) in enumerate(intervals):
            pos = bisearch(e)
            ans += pos-i-1

        return ans
