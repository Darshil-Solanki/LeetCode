class Solution:
    def alternatingSum(self, nums: List[int]) -> int:
        even = odd = 0
        for i in range(0, len(nums), 2):
            even += nums[i]

        for i in range(1, len(nums), 2):
            odd += nums[i]

        return even - odd
