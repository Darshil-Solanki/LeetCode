class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        d = {}
        for num in nums:
            if num in d:
                return num
            d[num] = True
