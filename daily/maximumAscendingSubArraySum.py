class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        maxSum = maxCurrSum = prev = nums[0]
        for i in range(1, len(nums)):
            curr = nums[i]
            if curr>prev:
                maxCurrSum+=curr
            else:
                maxCurrSum = curr
            if maxCurrSum>maxSum: maxSum = maxCurrSum
            prev = curr
        return maxSum
