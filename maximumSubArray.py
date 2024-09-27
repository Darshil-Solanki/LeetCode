class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_curr = max_global = nums[0]
        for i in range(1,len(nums)):
            max_curr = max(nums[i], max_curr+nums[i])
            if max_curr>max_global:
                max_global = max_curr
        return max_global

        # Slightly faster version
        # max_curr = 0
        # max_global = float('-inf')
        # for i in range(len(nums)):
        #     max_curr+=nums[i]
        #     if max_curr>max_global:
        #         max_global=max_curr
        #     if max_curr<0:
        #         max_curr=0
        # return max_global
        
