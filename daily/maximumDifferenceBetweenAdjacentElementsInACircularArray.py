class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        ans = 0
        prev = nums[0]
        for i in range(1, len(nums)):
            ans = max(ans, abs(prev-nums[i]))
            prev = nums[i]
        return max(ans, abs(nums[0]-nums[-1]))
