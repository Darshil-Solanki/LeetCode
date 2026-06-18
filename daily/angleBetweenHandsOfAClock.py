class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        hour_angle = 30*hour + 0.5*minutes
        minute_angle = 6*minutes
        diff = abs(minute_angle-hour_angle)
        return min(diff, 360-diff)
