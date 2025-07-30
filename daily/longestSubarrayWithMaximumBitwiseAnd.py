class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        max_num = max(nums)
        ans = count = 0
        
        for num in nums:
            if num == max_num:
                count += 1
                ans = max(ans, count)
            else:
                count = 0
        
        return ans
