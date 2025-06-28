class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        indexed_nums = list(enumerate(nums))
        indexed_nums.sort(key = lambda x: -x[1])
        return [num for i, num in sorted(indexed_nums[:k])]
