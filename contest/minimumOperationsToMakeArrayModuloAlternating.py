class Solution:
    def minOperations(self, a: list[int], k: int) -> int:
        n = len(a)
        ans = 10 ** 9
        for x in range(k):
            for y in range(k):
                if x != y:
                    c = 0
                    for i in range(n):
                        if i & 1:
                            z = abs(a[i] % k - x)
                            c += min(z, k - z)
                        else:
                            z = abs(a[i] % k - y)
                            c += min(z, k - z)
                    ans = min(ans, c)
        return ans
