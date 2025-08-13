class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        return n>0 and 1162261467%n == 0
        # highest power in constraint will always be divisible by other smaller power only because all factor are 3 of powers
