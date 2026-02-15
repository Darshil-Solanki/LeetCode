class Solution:
    def rob(self, nums: List[int], colors: List[int]) -> int:
        n = len(nums)
        @cache
        def dp(i, prevColor, flag):
            if i == n:
                return 0
            rob = 0
            if prevColor!=colors[i] or not flag:
                rob = nums[i]+dp(i+1, colors[i], True)
            not_rob = dp(i+1, colors[i], False)
            return max(rob, not_rob)

        return dp(0, 0, False)
