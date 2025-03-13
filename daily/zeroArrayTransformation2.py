class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        def check(k):
            diff_arr = [0]*(len(nums)+1)

            for i in range(k):
                start, end, val = queries[i]
                diff_arr[start] += val
                diff_arr[end+1] -= val

            prefix_sum = 0
            for i in range(len(nums)):
                prefix_sum+=diff_arr[i]
                if prefix_sum<nums[i]:
                    return False
            return True

        left, right = 0, len(queries)  

        if not check(right): return -1

        while left<=right:
            mid = (left+right)//2
            if check(mid):
                right = mid-1
            else:
                left = mid+1
        
        return left


        
