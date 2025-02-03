class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        prev = nums[0]
        ans = 1
        inc, dec = 1, 1
        for i in range(1,len(nums)):
            if prev<nums[i]:
                inc+=1
                dec=1
            elif prev==nums[i]:
                inc = dec = 1
            else:
                inc=1
                dec+=1
            if inc>ans: ans = inc
            if dec>ans: ans = dec
            prev = nums[i]
        return ans
