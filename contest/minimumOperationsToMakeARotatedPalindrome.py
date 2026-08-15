class Solution:
    def minOperations(self, s: str) -> int:
        ord_s = [ord(c)-97 for c in s]
        n = len(s)
        ans = float("inf")

        for i in range(n):
            rotated = ord_s[i:] + ord_s[:i]
            cost = i
            
            for j in range(n // 2):
                if cost>=ans:
                    break
                a, b = rotated[j], rotated[n-j-1]
                d = abs(a-b)
                cost += min(d, 26-d)

            if cost<ans:
                ans = cost
        
        return ans
