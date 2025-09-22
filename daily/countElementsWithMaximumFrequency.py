class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        cnt = Counter(nums)
        cnt = cnt.most_common()
        max_freq = cnt[0][1]
        ans = 0
        for _, f in cnt:
            if f<max_freq:
                break
            ans += f
        return ans
