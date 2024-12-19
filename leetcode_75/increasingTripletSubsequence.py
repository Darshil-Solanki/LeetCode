class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        smallest, small = float("inf"), float("inf")
        for i, curr in enumerate(nums):
            if curr>small: return True
            if curr<smallest:
                smallest = curr
            if smallest<curr<small:
                small = curr
        return False
