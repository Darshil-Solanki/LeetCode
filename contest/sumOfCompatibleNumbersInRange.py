class Solution:
    def sumOfGoodIntegers(self, n: int, k: int) -> int:
        tot = 0
        for num in range(max(n-k, 0), n+k+1):
            if num & n == 0:
                tot += num
        return tot
