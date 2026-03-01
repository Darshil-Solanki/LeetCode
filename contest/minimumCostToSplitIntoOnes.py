class Solution:
    @cache
    def minCost(self, n: int) -> int:
        if n == 1: return 0
        return n-1+self.minCost(n-1)
