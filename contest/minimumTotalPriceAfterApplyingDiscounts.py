class Solution:
    def minPrice(self, prices: list[int], discounts: list[int]) -> float:
        prices.sort(reverse=True)
        discounts.sort(reverse=True)
        len_p, len_d = len(prices), len(discounts)
        dis_prices = min(len_p, len_d)

        tot = 0
        for i in range(dis_prices):
            tot += (prices[i] * (100 - discounts[i])) / 100

        for i in range(dis_prices, len_p):
            tot += prices[i]

        return tot
