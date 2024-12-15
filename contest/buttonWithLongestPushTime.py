class Solution:
    def buttonWithLongestTime(self, events: List[List[int]]) -> int:
        maxIdx = 0
        maxT = 0
        prev = None
        for idx, (i, t) in enumerate(events):
            if not idx:
                maxIdx = i
                maxT = t
            else:
                if maxT < t-prev:
                    maxT = t-prev
                    maxIdx = i
                elif maxT == t-prev:
                    maxIdx = min(maxIdx, i)
            prev = t
        return maxIdx
