class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        j = 2
        ans = 2
        while j<len(nums):
            l = j-2
            while j<len(nums) and nums[j] == nums[j-1]+nums[j-2]:
                j+=1
            r = j
            ans = max(ans, r-l)
       
            j+=1

        return ans
