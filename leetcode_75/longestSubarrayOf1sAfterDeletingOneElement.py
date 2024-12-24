class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        l = res = 0
        zero = 1
        for r, n in enumerate(nums):
            if not n:
                zero-=1
            while zero<0:
                if not nums[l]:
                    zero+=1
                l+=1
            if r-l>res: res = r-l
        return  res-1 if len(nums)==res else res
