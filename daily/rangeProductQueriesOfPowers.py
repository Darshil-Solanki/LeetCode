class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        powers = []
        i = 0
        while n>0:
            if n & 1:
                powers.append(2**i)
            n = n>>1
            i+=1
        
        MOD = 1_000_000_007
        length = len(powers)
        cache = [[0]*length for _ in range(length)]

        for i, p in enumerate(powers):
            ans = p
            cache[i][i] = ans
            for j in range(i+1, length):
                ans = ans * powers[j] % MOD
                cache[i][j] = ans

        return [cache[left][right] for left, right in queries]
