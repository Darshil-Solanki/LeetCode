class Solution:
    def maxProfit(self, prices: List[int], strategy: List[int], k: int) -> int:
        prefix_sum = []
        temp = 0
        for p, s in zip(prices, strategy):
            temp += p*s
            prefix_sum.append(temp)
        
        original = max_profit = temp
        window_sum = prefix_sum[k-1]
        half_window_sum = sum(prices[k//2: k])
        max_profit = max(max_profit, original-window_sum+half_window_sum)

        for i in range(k, len(prices)):
            window_sum -= prices[i-k]*strategy[i-k]
            window_sum += prices[i]*strategy[i]
            half_window_sum -= prices[i-k//2]
            half_window_sum += prices[i]

            curr_prof = original-window_sum+half_window_sum
            max_profit = max(max_profit, curr_prof)

        return max_profit
