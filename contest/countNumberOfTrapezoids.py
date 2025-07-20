class Solution:
    def countTrapezoids(self, pts: List[List[int]]) -> int:
        #copied from contest
        mod = 10**9 + 7
        cnt = Counter(y for z, y in pts)
        t = [c * (c - 1) // 2 % mod for c in cnt.values() if c > 1]
        s = sum(t) % mod
        s2 = sum(x * x for x in t) % mod
        return (s * s - s2) * ((mod + 1) // 2) % mod
