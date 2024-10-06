class Solution:
    def maxGoodNumber(self, nums: List[int]) -> int:
        num1 = bin(nums[0])[2:]
        num2 = bin(nums[1])[2:]
        num3 = bin(nums[2])[2:]
        return max(int(num1+num2+num3,2), int(num1+num3+num2,2),
         int(num2+num1+num3,2), int(num2+num3+num1,2),
         int(num3+num1+num2,2), int(num3+num2+num1,2))
