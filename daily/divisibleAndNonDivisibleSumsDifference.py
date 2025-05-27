class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        divisible_sum = sum(range(m, n+1, m))
        # tot = sum(range(1, n+1))
        tot = n*(n+1)//2 # sum of n number of ap
        return tot - 2*divisible_sum
