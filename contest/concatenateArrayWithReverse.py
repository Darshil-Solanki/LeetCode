class Solution:
    def concatWithReverse(self, nums: list[int]) -> list[int]:
        nums.extend(reversed(nums))
        return nums
