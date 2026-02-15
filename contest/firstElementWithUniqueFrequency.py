class Solution:
    def firstUniqueFreq(self, nums: List[int]) -> int:
        cnt = Counter(nums)
        freq_cnt = Counter(cnt.values())
        for num in nums:
            if freq_cnt[cnt[num]]==1:
                return num
        return -1
