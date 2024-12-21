class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        ans = 0
        for i in range(1, len(nums)-1):
            first, second = nums[i-1], nums[i+1]
            if nums[i]/2==(first+second): ans +=1
        return ans
