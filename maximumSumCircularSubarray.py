class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        currMax = globalMax = tot = nums[0]
        currMin = globalMin = nums[0]
        for i in range(1, len(nums)):
            tot+=nums[i]
            currMax = max(nums[i], currMax+nums[i])
            currMin = min(nums[i], currMin+nums[i])
            if currMax>globalMax:
                globalMax = currMax
            if currMin<globalMin:
                globalMin = currMin
        if globalMax<0:
            return globalMax
        return max(tot-globalMin, globalMax)
