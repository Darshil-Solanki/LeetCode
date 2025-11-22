class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        return sum(1 for n in nums if n%3)
