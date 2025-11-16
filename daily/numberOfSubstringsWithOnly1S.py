class Solution:
    def numSub(self, s: str) -> int:
        MOD = 1_000_000_007
        ans = 0

        for substr in s.split("0"):
            if len(substr):
                n = len(substr)
                ans += ((n*(n+1))//2) % MOD
        
        return ans
