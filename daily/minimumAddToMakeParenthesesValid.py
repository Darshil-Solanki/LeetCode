class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        ans = 0
        open_b = 0
        
        for i, c in enumerate(s):
            if c == "(":
                open_b += 1
            else:
                if open_b > 0:
                    open_b -= 1
                else:
                    ans += 1
                    
        return ans + open_b
