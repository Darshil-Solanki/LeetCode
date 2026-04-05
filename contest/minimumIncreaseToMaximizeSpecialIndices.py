class Solution:
    def minIncrease(self, nums: List[int]) -> int:
        n = len(nums)
        mx_sp_idx = ceil(n/2-1)

        @cache
        def dp(i, sp_i):
            if sp_i == mx_sp_idx:
                return 0
            if i>=n-1:
                return float("inf")

            if nums[i-1]<nums[i]>nums[i+1]:
                return dp(i+2, sp_i+1)

            mx = max(nums[i-1], nums[i+1])
            temp, nums[i] = nums[i], mx+1
            change = mx+1-temp+dp(i+2, sp_i+1)
            nums[i] = temp
            not_change = dp(i+1, sp_i) if n-i-1>=(mx_sp_idx-sp_i)*2 else float("inf")
            return min(change, not_change)

        return dp(1, 0)
