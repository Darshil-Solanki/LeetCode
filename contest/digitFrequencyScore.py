class Solution:
    def digitFrequencyScore(self, n: int) -> int:
        cnt = Counter(str(n))
        return sum(int(c)*val for c, val in cnt.items())
