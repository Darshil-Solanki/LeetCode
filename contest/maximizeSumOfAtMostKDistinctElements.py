class Solution:
    def maxKDistinct(self, nums: List[int], k: int) -> List[int]:
        u_nums = list(set(nums))
        u_nums.sort(reverse=True)
        return u_nums[:k]
