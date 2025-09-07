class Solution:
    def minOperations(self, nums: List[int]) -> int:
        nums_set = set(nums)
        return 1 if len(nums_set)>1 else 0
