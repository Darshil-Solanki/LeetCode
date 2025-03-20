class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        n = len(nums)
        diff_arr = [0]*(n+1)
        prefix_sum = [0]*(n+1)
        for start, end in queries:
            diff_arr[start]+=1
            diff_arr[end+1]-=1
        
        prefix_sum = 0
        for i in range(n):
            prefix_sum+=diff_arr[i]
            if prefix_sum<nums[i]: return False
        
        return True
