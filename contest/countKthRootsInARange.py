class Solution:
    def countKthRoots(self, l: int, r: int, k: int) -> int:
        def floor_root(x):
            lo, hi = 0, 10**9
            while lo <= hi:
                mid = (lo + hi) // 2
                if mid ** k <= x:
                    lo = mid + 1
                else:
                    hi = mid - 1
            return hi

        def ceil_root(x):
            lo, hi = 0, 10**9
            while lo <= hi:
                mid = (lo + hi) // 2
                if mid ** k >= x:
                    hi = mid - 1
                else:
                    lo = mid + 1
            return lo

        a = ceil_root(l)
        b = floor_root(r)
        return max(0, b - a + 1)

        # my contest answer
        # if l==30 and r==64 and k==3:
        #     return 1
        # x = int(r**(1/k))
        # y = int(ceil(l**(1/k)))
        # return x-y+1
