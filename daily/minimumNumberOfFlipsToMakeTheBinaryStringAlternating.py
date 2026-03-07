class Solution:
    def minFlips(self, s: str) -> int:
        n = len(s)
        ans = n
        op = [0, 0]

        for i, c in enumerate(s):
            op[(ord(c) ^ i) & 1] += 1
        
        for i in range(n):
            c = ord(s[i])
            op[(c^i) & 1] -= 1
            op[(c^(n+i)) & 1] += 1
            ans = min(ans, min(op))
        
        return ans
