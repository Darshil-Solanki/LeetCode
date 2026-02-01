class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        min_1, min_2 = float("inf"), float("inf")
        for i in range(1, len(nums)):
            num = nums[i]
            if num<min_2 and num<min_1:
                min_1, min_2 = num, min_1
            elif num<min_2:
                min_2 = num
        return nums[0]+min_1+min_2
