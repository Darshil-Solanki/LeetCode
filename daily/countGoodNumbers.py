MOD = 1_000_000_007
@cache
def fast_exponential(b, p):
    ans, mul = 1, b
    while p>0:
        if p%2: #odd power
            ans = ans * mul % MOD
        mul = mul * mul % MOD
        p//=2
    return ans
class Solution:
    def countGoodNumbers(self, n: int) -> int:
        return fast_exponential(5, (n+1)//2) * fast_exponential(4, n//2) % MOD
