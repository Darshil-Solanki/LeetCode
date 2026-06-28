class Solution:
    def filterOccupiedIntervals(self, occupiedIntervals: List[List[int]], freeStart: int, freeEnd: int) -> List[List[int]]:
        intervals = list(sorted(occupiedIntervals))
        n = len(intervals)
        result = [intervals[0]]

        for i in range(1, n):
            curr_st, curr_ed = intervals[i]
            prev_st, prev_ed = result[-1]
            if prev_ed>=curr_st or prev_ed==curr_st-1:
                result[-1][1] = max(curr_ed, prev_ed)
            else:
                result.append([curr_st, curr_ed])

        result2 = []
        for a, b in result:
            new_st, new_ed = a, b
            if freeStart<=a<=freeEnd:
                new_st = freeEnd + 1
                if b<=freeEnd:
                    continue
                result2.append([new_st, new_ed])
            elif a<=freeStart<=b:
                new_ed = freeStart - 1
                result2.append([new_st, new_ed])
                if freeEnd<b:
                    result2.append([freeEnd+1, b])
            else:
                result2.append([new_st, new_ed])
                
        return result2
