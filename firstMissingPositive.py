class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        start = 1
        prev = None
        nums.sort()
        for i in nums:
            if i<=0:
                continue
            if i == prev:
                continue
            if i!=start:
                return start
            prev = i
            start+=1

        return start

        # Better Solution
        # n = len(nums)
        
        # # Step 1: Replace all invalid numbers
        # for i in range(n):
        #     while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
        #         # Swap nums[i] with nums[nums[i] - 1]
        #         nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
        
        # # Step 2: Identify the first missing positive number
        # for i in range(n):
        #     if nums[i] != i + 1:
        #         return i + 1
        
        # # If all positions are correctly filled, the missing number is n + 1
        # return n + 1
