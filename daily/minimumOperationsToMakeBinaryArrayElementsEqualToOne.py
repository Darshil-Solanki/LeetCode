class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        count = 0

        for i in range(n-2):
            if not nums[i]:
                nums[i], nums[i+1], nums[i+2] = 1, int(not nums[i+1]), int(not nums[i+2])
                count+=1
                
        if nums[n-1] and nums[n-2]: return count
        return -1
