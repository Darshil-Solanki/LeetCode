class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums.sort()
        j=1
        n=len(nums)
        while j<=n:
            if j==n:
                return nums[j-1]
            if nums[j]!=nums[j-1]:
                return nums[j-1]
            j+=2
