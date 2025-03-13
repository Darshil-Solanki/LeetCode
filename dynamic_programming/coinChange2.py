class Solution:
    def change(self, amount: int, coins: List[int]) -> int:

        dp_prev, dp_curr = [0]*(amount+1), [0]*(amount+1)
        dp_prev[0] = 1

        for coin_idx in range(len(coins)):
            dp_curr[0] = 1
            for amount in range(1, amount+1):
                if coins[coin_idx]>amount: continue
                dp_curr[amount] = dp_prev[amount]+dp_curr[amount-coins[coin_idx]]

            dp_prev = dp_curr[:]
        return dp_curr[amount]
        
        # @cache
        # def dp(amount, i):
        #     if amount == 0:
        #         return 1
            
        #     if amount>0 and i<len(coins):
        #         return dp(amount, i+1) + dp(amount-coins[i], i)
            
        #     return 0
        
        # return dp(amount, 0)
