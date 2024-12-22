from math import ceil
class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        a = set()
        for i in range(len(nums)-1, -1, -1):
            if nums[i] not in a:
                a.add(nums[i])
            else:
                return ceil((i+1)/3)
        return 0
