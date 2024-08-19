class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        if not n:
            return 0
        mx = 0
        pool = set()
        l=0
        for r in range(n):
            while s[r] in pool:
                pool.remove(s[l])
                l+=1
            pool.add(s[r])
            mx= r-l+1 if r-l+1>mx else mx
        return mx
