class Solution:
    def findGoodIntegers(self, n: int) -> list[int]:
        # copied from contest submission
        freq = defaultdict(int)
        a = 1
        while 2 * (a ** 3) <= n:
            b = a
            while (a ** 3) + (b ** 3) <= n:
                val = (a ** 3) + (b ** 3)
                freq[val] += 1
                b += 1
            a += 1
        return sorted(k for k, v in freq.items() if v >= 2)
