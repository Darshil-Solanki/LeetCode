class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        zero_count1, zero_count2 = nums1.count(0), nums2.count(0)
        sum1, sum2 = sum(nums1)+zero_count1, sum(nums2)+zero_count2
        
        if sum1 == sum2:
            return sum1

        if not zero_count1 and not zero_count2:
            return -1 

        if (not zero_count1 and sum2>sum1) or (not zero_count2 and sum1>sum2):
            return -1
        
        return sum1 if sum1>sum2 else sum2
