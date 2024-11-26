class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort()
        dp = [float("inf")]*(amount+1)
        dp[0]=0
        for currAmt in range(1, amount+1):
            for coin in coins:
                if currAmt-coin<0:
                    break
                dp[currAmt]=min(dp[currAmt], 1+dp[currAmt-coin])
        return dp[amount] if dp[amount]!=float("inf") else -1           
    
    # Better Solution using bitmasking in dp
    # def coinChange(self, coins: List[int], n: int) -> int:
    #     if not n: return 0
    #     coins = [c for c in coins if c<=n]
    #     if not coins: return -1
    #     if len(coins)==1:
    #         return -1 if n%coins[0] else n//coins[0]
    #     if n & 1 and not any(c & 1 for c in coins): return -1
    #     subAmountArray = 1 << n 
    #     for i in range(1, n ):
    #         cur = subAmountArray
    #         for coin in coins:
    #             subAmountArray |= cur >> coin
    #         if subAmountArray & 1:
    #             return i
    #         if cur == subAmountArray: return -1
