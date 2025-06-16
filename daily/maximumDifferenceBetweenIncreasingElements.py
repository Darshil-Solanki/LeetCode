class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        ans = -1
        min_num = float("inf")

        for i in range(len(nums)):
            if nums[i]<min_num:
                min_num = nums[i]
            else:
                ans = max(ans, nums[i]-min_num)
        
        return ans if ans else -1
