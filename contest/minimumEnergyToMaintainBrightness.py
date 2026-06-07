class Solution:
    def minEnergy(self, n: int, brightness: int, intervals: list[list[int]]) -> int:
        min_on_bulb = n//3
        if n%3:
            min_on_bulb += 1

        min_on_bulb = min(min_on_bulb, (brightness//3) + (1 if brightness%3 else 0)) if brightness>2 else 1
        
        intervals.sort()
        new_intervals = [intervals[0]]
        for i in range(1, len(intervals)):
            prev_s, prev_e = new_intervals[-1]
            curr_s, curr_e = intervals[i]
            if curr_s<=prev_e:
                new_intervals[-1][1] = max(curr_e, prev_e)
            else:
                new_intervals.append(intervals[i])

        return sum((e-s+1)*min_on_bulb for s, e in new_intervals)
