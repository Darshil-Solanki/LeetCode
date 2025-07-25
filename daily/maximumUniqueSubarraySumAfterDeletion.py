class Solution:
    def maxSum(self, nums: List[int]) -> int:
        positiveSet = set([num for num in nums if num>0])
        return sum(positiveSet) if positiveSet else max(nums)
