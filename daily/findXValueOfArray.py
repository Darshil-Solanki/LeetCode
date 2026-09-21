class Solution:
    def resultArray(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        ans = [0] * k
        dp = [0] * k

        for i in range(n):
            curr_dp = [0] * k
            curr_dp[nums[i] % k] += 1
            for r in range(k):
                curr_dp[(r * nums[i]) % k] += dp[r]
            
            dp = curr_dp

            for r in range(k):
                ans[r] += dp[r]
        
        return ans
