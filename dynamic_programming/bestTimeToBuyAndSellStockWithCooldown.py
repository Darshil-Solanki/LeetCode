class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        memo = {}
        
        def dp(i, state):
            if i == n:
                return  0  # If ended on a buy or cooldown, no profit
            
            if (i, state) in memo:
                return memo[(i, state)]
            
            if state == 0:  # Cooldown
                # Can either do nothing or buy today
                ans = dp(i+1, 1) 
            elif state == 1:  # Can buy
                # Either buy today or don't
                ans = max(dp(i+1, 1), dp(i+1, 2) - prices[i])
            else:  # state == 2, Just bought
                # Either sell today or don't
                ans = max(dp(i+1, 0) + prices[i], dp(i+1, 2))
            
            memo[(i, state)] = ans
            return ans
        
        # Start in state 1, where we can buy
        return dp(0, 1)

        # Space optimized tabulation
        # n = len(prices)
        # hold, free, reset = float('-inf'), float('-inf'), 0
        # for i in range(n):
        #     prefree = free
        #     free = hold + prices[i]
        #     hold = max(hold, reset - prices[i])
        #     reset = max(reset, prefree)
        
        # return max(free, reset)
