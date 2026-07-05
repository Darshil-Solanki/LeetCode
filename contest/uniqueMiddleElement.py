class Solution:
    def isMiddleElementUnique(self, nums: list[int]) -> bool:
        n = len(nums)
        cnt = Counter(nums)
        return cnt[nums[n//2]]==1
