class Solution:
    def findCoins(self, numWays: List[int]) -> List[int]:
        n = len(numWays)
        dp = [0]*(n+1)
        dp[0] = 1
        coins = []
        
        for i, ways in enumerate(numWays):
            amount = i+1
            if ways and dp[amount] == ways-1:
                coins.append(amount)
                for coin in range(amount, n+1):
                    dp[coin] += dp[coin-amount]
            
            if dp[amount] != ways: return []

        return coins
