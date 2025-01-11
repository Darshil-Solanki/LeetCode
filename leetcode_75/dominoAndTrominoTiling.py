class Solution:
    def numTilings(self, n: int) -> int:
        if n==3: return 5
        if n==2: return 2
        if n==1: return 1
        MOD = 1000000007
        first, second, third = 1, 2, 5
        for i in range(n-3):
            first, second, third = second, third, (2*third+first)%MOD
        return third
