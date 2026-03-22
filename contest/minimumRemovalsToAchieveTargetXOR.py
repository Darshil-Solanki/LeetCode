class Solution:
    def minRemovals(self, nums: List[int], target: int) -> int:
        n = len(nums)
        xor = 0
        
        for num in nums:
            xor ^= num
        
        @cache
        def helper(i, xr):
            if i == n:
                if xr == target:
                    return 0
                return float("inf")

            ans1 = helper(i+1, xr^nums[i])
            ans2 = helper(i+1, xr)

            return min(ans1+1, ans2)

        ans = helper(0, xor)
        return -1 if ans==float("inf") else ans
