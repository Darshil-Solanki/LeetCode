class Solution:
    def minCost(self, nums: list[int]) -> int:
        n = len(nums)
        ans = float("inf")

        start = 0
        while start < n:
            end = start + 1
            while end < n and nums[end] == nums[start]:
                end += 1
            
            group_length = end - start
            
            if start < n-1 and end > 1:
                cost = (n - group_length) * nums[start]
                ans = min(ans, cost)
            
            start = end
        
        return 0 if ans == float("inf") else ans

