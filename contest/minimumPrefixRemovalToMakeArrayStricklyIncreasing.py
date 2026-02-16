class Solution:
    def minimumPrefixLength(self, nums: List[int]) -> int:
        ans = 0
        for i in range(len(nums)-1):
            if nums[i]>=nums[i+1]:
                ans = i+1
        
        return ans
