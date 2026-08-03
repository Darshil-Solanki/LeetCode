class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        n = len(stoneValue)

        @cache
        def dp(i):
            if i == n:
                return 0
            a = b = c = float("-inf")

            a = stoneValue[i] - dp(i+1)
            if i+1 < n:
                b = stoneValue[i] + stoneValue[i+1] - dp(i+2)
            if i + 2 < n:
                c = stoneValue[i] + stoneValue[i+1] + stoneValue[i+2] - dp(i+3)
            
            return max(a, b, c)
        
        d = dp(0)
        if d>0:
            return "Alice"
        if d<0:
            return "Bob"
        return "Tie"
