class Solution:
    def minInsertions(self, s: str) -> int:
        open_b, idx, n = 0, 0, len(s)
        ans = 0

        while idx < n:
            if s[idx] == "(":
                open_b += 1
            else:
                if open_b:
                    open_b -= 1
                else:
                    ans += 1

                if idx < n-1 and s[idx+1]==")":
                    idx += 1
                else:
                    ans += 1
            
            idx += 1
                
        return ans + open_b * 2
