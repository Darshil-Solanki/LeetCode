class Solution:
    def processStr(self, s: str, k: int) -> str:
        n = 0
        for c in s:
            if c == "*":
                if n:
                    n -= 1
            elif c == "#":
                n += n
            elif c == "%":
                pass
            else:
                n += 1
        if k+1>n:
            return "."
        
        for c in reversed(s):
            if c == "*":
                n += 1
            elif c == "#":
                if k+1>(n+1)//2:
                    k -= n//2
                n = (n+1)//2
            elif c == "%":
                k = n-k-1
            else:
                if k+1 == n:
                    return c
                n -= 1
        return "."
