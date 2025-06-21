class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        cnt = Counter(word)
        ans = len(word)

        for a, cnt_a in cnt.items():
            deleted = 0
            for b, cnt_b in cnt.items():
                if cnt_a > cnt_b:
                    deleted += cnt_b
                elif cnt_b > cnt_a + k:
                    deleted += cnt_b-(cnt_a+k)
            ans = min(ans, deleted)
        
        return ans
