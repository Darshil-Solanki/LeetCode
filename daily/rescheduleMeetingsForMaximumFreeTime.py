class Solution:
    def maxFreeTime(self, eventTime: int, k: int, startTime: List[int], endTime: List[int]) -> int:
        n = len(startTime)
        duration_pre_sum = [0]*(n+1)

        for i in range(n):
            duration_pre_sum[i+1] = duration_pre_sum[i] + endTime[i]-startTime[i]

        ans = 0
        for i in range(k-1, n):
            left = 0 if i==k-1 else endTime[i-k]
            right = eventTime if i==n-1 else startTime[i+1]
            total = right-left-(duration_pre_sum[i+1]-duration_pre_sum[i-k+1])
            ans = max(ans, total)
        
        return ans
