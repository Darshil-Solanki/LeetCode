class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        cnt = Counter(costs)
        mx_cost = max(costs)
        ans = 0

        for price in range(1, mx_cost+1):
            if cnt[price]:
                if coins<price:
                    break
                buy = min(coins//price, cnt[price])
                ans += buy
                coins -= buy*price
        
        return ans

        # NLog(N) 
        # cnt = Counter(costs)
        # ans = 0

        # for c, freq in sorted(cnt.items()):
        #     if not freq:
        #         continue
        #     buy = min(coins//c, freq)
        #     if not buy:
        #         break
        #     ans += buy
        #     coins -= buy*c
        
        # return ans
