class Solution:
    def tribonacci(self, n: int) -> int:
        t0, t1, t2 = 0, 1, 1
        if not n: return 0
        if n==1 or n==2: return 1
        for i in range(n-2):
            t0, t1, t2, = t1, t2, t0+t1+t2
        return t2
