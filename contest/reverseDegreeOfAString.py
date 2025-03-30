class Solution:
    def reverseDegree(self, s: str) -> int:
        ans = 0
        for i,c in enumerate(s):
            ans += (26 -(ord(c)-97))*(i+1)
        return ans
        # return sum( (26-(ord(c)-97))*(i+1) for i, c in enumerate(s))
