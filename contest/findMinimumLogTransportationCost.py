class Solution:
    def minCuttingCost(self, n: int, m: int, k: int) -> int:
        ans = 0
        while n>k:
            ans += n*k-k*k
            n-=k
        while m>k:
            ans += m*k-k*k
            m -= k
        return ans
