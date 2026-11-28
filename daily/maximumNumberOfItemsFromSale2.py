class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        items.sort(key = lambda x: x[1])
        mx_factor = max(f for f, _ in items)
        freq = [0] * (mx_factor + 1)

        for f, _ in items:
            freq[f] += 1
        
        for i in range(1, mx_factor + 1):
            if freq[i] > 0:
                for j in range(i * 2, mx_factor+1, i):
                    freq[i] += freq[j]
        
        mn_price = items[0][1]
        ans = 0
        for factor, price in items:
            if price > mn_price * 2:
                break
            cnt = freq[factor] - 1
            take = min(cnt, budget//price)
            ans += take * 2
            budget -= take * price
        
        ans += budget // mn_price

        return ans
