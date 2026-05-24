class Solution:
    def limitOccurrences(self, nums: list[int], k: int) -> list[int]:
        cnt = defaultdict(int)
        ans = []
        for num in nums:
            if cnt[num]==k:
                continue
            cnt[num] += 1
            ans.append(num)
        return ans
