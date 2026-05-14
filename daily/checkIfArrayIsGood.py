class Solution:
    def isGood(self, nums: List[int]) -> bool:
        n = len(nums)-1
        cnt = Counter(nums)
        for i in range(1, n):
            if i not in cnt:
                return False
        if cnt[n]==2:
            return True
        return False
