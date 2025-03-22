class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        MOD = 1_000_000_007
        dp = [0]*(high+1)
        dp[0]=1

        for i in range(1, low):
            dp_zero = dp[i-zero] if i-zero>-1 else 0
            dp_one = dp[i-one] if i-one>-1 else 0
            dp[i] = dp_zero+dp_one

        ans = 0
        for i in range(low, high+1):
            dp_zero = dp[i-zero] if i-zero>-1 else 0
            dp_one = dp[i-one] if i-one>-1 else 0
            dp[i] = (dp_zero+dp_one)%MOD
            ans+=dp[i]

        return ans%MOD

        # with @cache memory limit exceeded with all testcases passed
        # @lru_cache
        # def dp(i):
        #     if i==0: return 1
        #     if i<0: return 0
            
        #     return dp(i-zero)+dp(i-one)

        # ans = 0
        # for i in range(low, high+1):
        #     ans+=(dp(i)%MOD)
        
        # return ans%MOD

        # finding min and max of zero and one because each mulitple of min of zero and one length till max of both value can only be one string which remove reduce the time complexity as for second loop we don't have to if i-zero and i-one is greater than 0
        # x = min(zero, one)
        # y = max(zero, one)
        # MOD = 10 ** 9 + 7
        # dp = [0] * (high + 1)
        # for i in range(0, y, x):
        #     dp[i] = 1
        # for i in range(y, high + 1):
        #     dp[i] = (dp[i - x] + dp[i - y]) % MOD
        # return sum(dp[low:high + 1]) % MOD
