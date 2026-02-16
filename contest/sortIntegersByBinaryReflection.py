class Solution:
    def sortByReflection(self, nums: List[int]) -> List[int]:
        for i, n in enumerate(nums):
            nums[i] = (n, int((bin(n)[2:])[::-1], 2))

        nums.sort(key = lambda x: (x[1], x[0]))
        return [n[0] for n in nums]
