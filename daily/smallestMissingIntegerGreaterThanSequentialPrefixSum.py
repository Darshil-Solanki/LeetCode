class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        prefix = nums[0]
        for i in range(1,len(nums)):
            if nums[i] != nums[i-1] + 1:
                break
            prefix += nums[i]
        
        s = set(nums)
        while True:
            if prefix not in s:
                return prefix
            prefix += 1
