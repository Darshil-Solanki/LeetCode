class Solution:
    def minDeletions(self, nums: list[int]) -> int:
        n = len(nums)

        @cache
        def dp(i, last):
            if i == n:
                return 0

            keep = dp(i+1, nums[i]) if (i==0 or (nums[i]^last != 0)) else float("inf")
            not_keep = 1+dp(i+1, last)
            
            return min(keep, not_keep)

        return dp(0, 0)
