class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        ans, left = 0, 0
        prev = prices[0]+1

        for right, p in enumerate(prices):
            if prev==p+1:
                ans += (right-left+1)
            else:
                left = right
                ans += 1
            prev = p

        return ans
