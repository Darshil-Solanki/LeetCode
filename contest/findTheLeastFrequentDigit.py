class Solution:
    def getLeastFrequentDigit(self, n: int) -> int:
        cnt = Counter(str(n))
        ans, least_count = -1, float("inf")
        for i in "0123456789":
            if cnt[i] and cnt[i]<least_count:
                least_count = cnt[i]
                ans = i        
        return int(ans)
