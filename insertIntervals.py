class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]
        l, r = 0, len(intervals)-1
        n = len(intervals)
        prevL, prevR = l, r
        while l<=r:
            if intervals[l][1]<newInterval[0]:
                l+=1
            if intervals[r][0]>newInterval[1]:
                r-=1
            if (prevL==l and prevR==r) or (l>=n or r<0):
                break
            prevL, prevR = l, r
        if l>=n:
            return intervals+[newInterval]
        if r<=-1:
            return [newInterval]+intervals
        return intervals[:l]+ [ [min(intervals[l][0], newInterval[0]), max(intervals[r][1], newInterval[1])] ] + intervals[r+1:] 
