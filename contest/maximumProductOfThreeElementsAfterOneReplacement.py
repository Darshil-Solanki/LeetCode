class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        nums.sort()
        nums = [n for n in nums if n]
        if len(nums)<2: return 0
        min_two_product = nums[0]*nums[1]
        max_two_product = nums[-2]*nums[-1]
        min_max_product = nums[0]*nums[-1]
        return max(abs(min_two_product)*100_000, abs(max_two_product)*100_000, abs(min_max_product)*100_000)
