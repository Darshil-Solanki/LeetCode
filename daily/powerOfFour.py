class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n<1: return False
        num = log(n, 4)
        return int(num)==num
