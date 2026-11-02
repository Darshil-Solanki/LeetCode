class Solution:
    def minMoves2(self, nums: list[int]) -> int:
        nums.sort()
        n = len(nums)
        mid = nums[n // 2]
        
        return sum(abs(mid-num) for num in nums)
