class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x: x[1])
        prevX, prevY = intervals[0][0], intervals[0][1]
        count = 0
        for i in range(1, len(intervals)):
            x, y = intervals[i][0], intervals[i][1]
            if x<prevY:
                count+=1
                continue
            prevX, prevY = x,y
        return count

        # faster method from submission
        # counting only non-overlapping interval
        # min_end, count = -inf, 0
        # for start, end in sorted(intervals, key=itemgetter(1)):
        #     if min_end <= start:
        #         min_end = end
        #         count += 1
        # return len(intervals) - count
