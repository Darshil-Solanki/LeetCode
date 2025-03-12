class Solution:
    def numSquares(self, n: int) -> int:
        max_sq = int(n**0.5)
        squares = [s*s for s in range(1, max_sq+1)]
        dp = [n]*(n+1)
        dp[0] = 0

        for target in range(1, n+1):
            for s in squares:
                if s>target:
                    break
                dp[target] = min(dp[target], 1+dp[target-s])
        
        return dp[n]
           

        # def dp(curr):
        #     if curr == 0:
        #         return 0
            
        #     if curr in memo:
        #         return memo[curr]
                
        #     ans  = float("inf")
        #     for s in squares:
        #         if curr-s<0:
        #             break
        #         ans = min(ans, dp(curr-s)+1)
            
        #     memo[curr] = ans
        #     return ans

        # memo = {}
        # return dp(n)
