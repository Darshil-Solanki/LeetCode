class Solution:
    def maxDifference(self, nums: list[int]) -> int:
        n = len(nums)

        @cache
        def dp(i):
            if i == n:
                return 0

            future = dp(i+1)
            best = nums[i] + (-future if nums[i] % 3 == 0 else future)

            if i+1<n:
                future = dp(i+2)
                best = max(best, nums[i] + nums[i+1] + (-future if (nums[i] + nums[i+1]) % 3 == 0 else future))

            return best

        return dp(0)
