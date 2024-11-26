class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        totProfit = 0
        buyPrice, profit = prices[0], 0
        for price in prices:
            if price<buyPrice:
                buyPrice=price
            elif price-buyPrice>profit:
                totProfit+=price-buyPrice
                buyPrice = price
                profit = 0
        return totProfit
