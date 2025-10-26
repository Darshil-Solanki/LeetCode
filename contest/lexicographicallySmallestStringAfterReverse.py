class Solution:
    def lexSmallest(self, s: str) -> str:
        ans = s
        l = list(s)
        n = len(s)
        for i in range(1, n+1):
            first = "".join(list(reversed(l[:i]))+l[i:])
            second = "".join(l[:-i]+list(reversed(l[-i:])))
            ans = min(ans, first, second)
        return ans

        # faster approach from submission
        # n = len(s)
        # smallest = s
        # r_s = s[::-1]
        # for i in range(1, n+1):
        #     a = r_s[-i:] + s[i:]
        #     b = s[:n-i] + r_s[:i]
        #     smallest = min(smallest, a, b)
        # return smallest
