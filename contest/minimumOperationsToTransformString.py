class Solution:
    def minOperations(self, s: str) -> int:
        cnt = Counter(s)
        ans = 0
        for c in range(98, 123):
            ch = chr(c)
            if cnt[ch]:
                ans += 1
                cnt[chr((c+1)%123)] += cnt[ch]
                del cnt[ch]

        return ans
