class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        num_set = set(nums)

        while True:
            if original not in num_set:
                return original
            original *= 2
