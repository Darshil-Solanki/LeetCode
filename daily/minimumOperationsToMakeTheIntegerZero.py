class Solution:
    def makeTheIntegerZero(self, num1: int, num2: int) -> int:
        if num2>num1: return -1
        k = 1
        while True:
            x = num1 - num2 * k
            if x<k:
                return -1
            if k>=x.bit_count():
                return k
            k += 1
