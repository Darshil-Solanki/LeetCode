class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buyPrice, profit = prices[0], 0
        for price in prices:
            if price<buyPrice:
                buyPrice = price
            elif price-buyPrice>profit:
                profit = price-buyPrice
        return profit
        
        
             
        
        # for i in range(len(prices)-1,-1,-1):
        #     for j in range(i,-1,-1):
        #         maxProf = prices[i]-prices[j] if prices[i]-prices[j]>maxProf else maxProf
        # return maxProf
        
                
        
