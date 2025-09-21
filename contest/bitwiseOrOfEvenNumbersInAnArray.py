class Solution:
    def evenNumberBitwiseORs(self, nums: List[int]) -> int:
        bor = 0
        for num in nums:
            if num%2==0:
                bor |= num
        return bor
