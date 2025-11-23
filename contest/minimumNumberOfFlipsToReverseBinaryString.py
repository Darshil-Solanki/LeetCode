class Solution:
    def minimumFlips(self, n: int) -> int:
        original = bin(n)[2:]
        reverse = original[::-1]
        return sum(1 for o, r in zip(original, reverse) if o!=r)
