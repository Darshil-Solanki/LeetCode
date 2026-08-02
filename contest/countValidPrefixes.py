class Solution:
    def countValidPrefixes(self, s: str) -> int:
        zero, one = 0, 0
        ans = 0
        
        for c in s:
            if c == "0":
                zero += 1
            else:
                one += 1
            if abs(zero-one) < 2:
                ans += 1
        
        return ans
