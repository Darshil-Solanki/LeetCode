class Solution:
    def maxFreeTime(self, eventTime: int, startTime: List[int], endTime: List[int]) -> int:
        ans = 0
        n = len(startTime)
        left_max_free_slot, right_max_free_slot = 0, 0
        duration = [0]*n
        can_shifted = [False]*n

        for i in range(n):
            duration[i] = endTime[i]-startTime[i]
            if duration[i]<=left_max_free_slot:
                can_shifted[i] = True
            
            left_max_free_slot = max(left_max_free_slot, startTime[i]-(0 if i==0 else endTime[i-1]))

            if endTime[n-i-1]-startTime[n-i-1] <= right_max_free_slot:
                can_shifted[n-i-1] = True
            right_max_free_slot = max(right_max_free_slot, (eventTime if i == 0 else startTime[n-i])-endTime[n-i-1])

        ans = 0
        for i in range(n):
            left = 0 if i == 0 else endTime[i-1]
            right = eventTime if i == n-1 else startTime[i+1]
            ans = max(ans, (right-left if can_shifted[i] else right-left-duration[i]))
        
        return ans
