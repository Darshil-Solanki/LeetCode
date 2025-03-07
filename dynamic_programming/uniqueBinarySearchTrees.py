class Solution:
    def numTrees(self, n: int) -> int:
        memo  = {}
        
        def dp(n):
            if n==0 or n==1: return 1

            if n in memo:
                return memo[n]

            ans = 0

            for i in range(n):
                ans += dp(i)*dp(n-i-1)


            memo[n] = ans
            return ans
        
        return dp(n)

        # dp =  [0]*(n+1)
        # dp[0] = dp[1] =1

        # for i in range(2, n+1):
        #     for left in range(1, i+1):
        #         dp[i] += dp[left-1]*dp[i-left]
        
        # return dp[n]
