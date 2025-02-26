class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        max_curr = min_curr = 0
        max_global, min_global = float("-inf"), float("inf")
        
        for num in nums:
            max_curr = max(num, max_curr+num)
            min_curr = min(num, min_curr+num)
            
            if max_curr>max_global: max_global = max_curr
            if min_curr<min_global: min_global = min_curr
            
        return max(max_global, abs(min_global))

        # Faster than Kadane algo
        # Prefix Sum 
        # s = list(accumulate(nums, initial=0))
        # return max(s) - min(s)
