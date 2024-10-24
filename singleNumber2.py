class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ones = twos = 0
        for n in nums:
            # adding to ones if not in twos
            ones = ones^n & ~twos
            # adding to ones if not in ones 
            twos = twos^n & ~ones
        return ones
