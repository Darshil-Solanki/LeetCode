class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [ [0]*3 for j in range(2) ]
        afterdp = [ [0]*3 for j in range(2) ]
        for i in range(n-1, -1, -1):
            for buy in range(2):
                for cap in range(1, 3):
                    if buy:
                        dp[buy][cap] = max(-prices[i]+afterdp[0][cap], afterdp[1][cap])
                    else:
                        dp[buy][cap] = max(prices[i]+afterdp[1][cap-1], afterdp[0][cap])
            afterdp = dp

        return afterdp[1][2]

        # Copied from Submission 
        # buy1, buy2 = float("inf"), float("inf")
        # profit1, profit2 = 0,0
        # for i in range(len(prices)):
        #     if buy1 > prices[i]:
        #         buy1 = prices[i]
        #     if profit1 < (prices[i] - buy1):
        #         profit1 = (prices[i] - buy1)
        #     if buy2 > prices[i] - profit1:
        #         buy2 = prices[i] - profit1
        #     if profit2 < (prices[i] - buy2):
        #         profit2 = (prices[i] - buy2)
            
        # return profit2


        # learn from youtube take U forward
        # n = len(prices)
        # dp = [ [[0]*3 for j in range(2)] for i in range(n+1) ]
        # for i in range(n-1, -1, -1):
        #     for buy in range(2):
        #         for cap in range(1, 3):
        #             if buy:
        #                 dp[i][buy][cap]=max(-prices[i]+dp[i+1][0][cap], dp[i+1][1][cap])
        #             else:
        #                 dp[i][buy][cap]=max(prices[i]+dp[i+1][1][cap-1], dp[i+1][0][cap])
        # return dp[0][1][2]

        # def dp(i, buy, cap):
        #     if cap==0: return 0
        #     if i==len(prices): return 0
        #     if buy and cap>0:
        #         return max(-prices[i]+dp(i+1, 0, cap), 0+dp(i+1, 1, cap))
        #     else:
        #         return max(0+dp(i+1, 0, cap), prices[i]+dp(i+1, 1, cap-1))
        
        # return dp(0, 1, 2)
