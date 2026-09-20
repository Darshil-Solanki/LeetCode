class Solution:
    def countIntersectingIntervals(self, intervals: list[list[int]]) -> int:
        ans = 0
        n = len(intervals)
        intervals.sort()
        for i in range(n):
            _, ie = intervals[i]
            for j in range(i+1, n):
                if ie>=intervals[j][0]:
                    ans += 1

        return ans
