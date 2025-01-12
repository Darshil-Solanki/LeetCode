class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)
        dp = [[0]*2 for _ in range(n+1)]
        for i in range(len(prices)-1, -1, -1):
            for buy in range(2):
                if buy:
                    dp[i][1] = max(-prices[i] + dp[i+1][0], dp[i+1][1])
                else:
                    dp[i][0] = max(prices[i]-fee+dp[i+1][1], dp[i+1][0])
        return dp[0][1]

        # copied from submission
        # buy = float('-inf')
        # sell = 0

        # for price in prices:
        #     buy = max(buy, sell - price)
        #     sell = max(sell, buy + price - fee)

        # return sell
