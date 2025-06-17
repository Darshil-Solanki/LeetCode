MOD = 1_000_000_007
MAX = 100_000

def fast_expo(x, n):
    res = 1
    while n:
        if n & 1:
            res = res * x % MOD
        x = x * x % MOD
        n >>=1
    return res

fact = [0]*MAX
inv_fact = [0]*MAX # factorial of inverse (1/x)!

fact[0] = 1
for i in range(1, MAX):
    fact[i] = fact[i-1]*i % MOD

inv_fact[MAX-1] =  fast_expo(fact[MAX-1], MOD-2)
for i in range(MAX-1, 0, -1):
    inv_fact[i-1] = inv_fact[i]*i % MOD

def comb(n, m):
    return fact[n] * inv_fact[m] % MOD * inv_fact[n-m] % MOD


class Solution:
    def countGoodArrays(self, n: int, m: int, k: int) -> int:
        return m * comb(n-1, k) % MOD * fast_expo(m-1, n-k-1) % MOD
