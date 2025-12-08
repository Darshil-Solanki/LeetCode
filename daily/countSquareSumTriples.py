class Solution:
    def countTriples(self, n: int) -> int:
        ans = 0
        for a in range(1, n+1):
            for b in range(a+1, n+1):
                c = a*a + b*b
                c_sqrt = int(sqrt(c))
                if c_sqrt<=n and c_sqrt*c_sqrt == c:
                    ans += 2 
        return ans
