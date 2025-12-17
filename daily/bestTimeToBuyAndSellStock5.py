class Solution:
    def maximumProfit(self, prices: List[int], k: int) -> int:
        n = len(prices)
        dp = [[0, -prices[0], prices[0]] for _ in range(k+1)]
        dp[0] = [0, 0, 0]
        
        for i in range(1, n):
            p = prices[i]
            for j in range(k, 0, -1):
                dp[j][0] = max(dp[j][0], dp[j][1]+p, dp[j][2]-p)
                dp[j][1] = max(dp[j][1], dp[j-1][0]-p)
                dp[j][2] = max(dp[j][2], dp[j-1][0]+p)            
        return dp[k][0]

        # @cache
        # def dp(i, j, state):
        #     if j == 0:
        #         return 0
        #     if i == 0:
        #         return (0 if state == 0 else -prices[0] if state == 1 else prices[0])
        #     p = prices[i]
        #     match state:
        #         case 0:
        #             ans = max(dp(i-1, j, 0), dp(i-1, j, 1)+p, dp(i-1, j, 2)-p)
        #         case 1:
        #             ans = max(dp(i-1, j, 1), dp(i-1, j-1, 0)-p)
        #         case 2:
        #             ans = max(dp(i-1, j, 2), dp(i-1, j-1, 0)+p)
        #     return ans

        # ans = dp(n-1, k, 0)
        # dp.cache_clear()
        # return ans
