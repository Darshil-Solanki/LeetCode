class Solution:
    def compareBitonicSums(self, nums: list[int]) -> int:
        total = sum(nums)
        left = 0
        peak = -1
        for i in range(len(nums)-1):
            if nums[i]<nums[i+1]:
                left += nums[i]
                continue
            peak = nums[i]
            left += peak
            break

        right = total - left + peak
        if left>right:
            return 0
        elif left<right:
            return 1
        else:
            return -1
