class Solution:
    def countOdds(self, low: int, high: int) -> int:
        ans = (high-low+1)//2
        if low%2 and (high-low+1)%2:
            ans += 1
        return ans
