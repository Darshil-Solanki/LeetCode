class Solution:
    def minPenalty(self, period: int, lights: list[int], arrivalTime: list[int]) -> int:
        ans = 0
        lights.sort()
        n = len(lights)
        
        for at in arrivalTime:
            r = at % period
            pos = bisect_right(lights, r)
            min_waiting_time = 0 if pos<n else period - r
            ans = max(ans, min_waiting_time)

        return ans
