class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        LIS = [1]*len(nums)
        for i in range(len(nums)-1, -1, -1):
            for j in range(i+1,len(nums)):
                if nums[i]<nums[j]:
                    LIS[i] = max(LIS[i], 1+LIS[j])
        return max(LIS)
    
    # Better efficient code Copied from Submission 
    # usage concept of adding highest element to end and replace in-between element to its position thus reducing time complexity from n square(for above code) to O(nlogn)
    # def lengthOfLIS(self, nums: List[int]) -> int:
    #     sub = []
    #     for num in nums:
    #         pos = bisect_left(sub, num)
    #         if pos == len(sub):
    #             sub.append(num)
    #             continue
    #         sub[pos] = num
    #     return len(sub)

# My initial recursive solution recurive calls 2 to power n times 
# class Solution:
#     def lengthOfLIS(self, nums: List[int]) -> int:
#         n = len(nums)-1
#         minVal = -10001
#         if n==0: return 1
#         def dp(value, length, i):
#             if i==0:
#                 return max(dp(nums[0],1,1), dp(minVal,0,1))
#             if i==n:
#                 return length+1 if nums[i]>value else length
#             if nums[i]<=value:
#                 return max(dp(value, length, i+1), dp(minVal,0,i+1))
#             else:
#                 return max(dp(nums[i], length+1, i+1), # dp(value,length,i+1))
#         return dp(nums[0],0,0)
