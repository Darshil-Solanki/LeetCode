class Solution:
    def peakValleyDifference(self, nums: list[int]) -> int:
        n = len(nums)
        peak, valley = 0, 0
        
        for i in range(1, n-1):
            if nums[i-1]<nums[i]>nums[i+1]:
                peak += nums[i]
            if nums[i-1]>nums[i]<nums[i+1]:
                valley += nums[i]

        return peak - valley
