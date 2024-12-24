class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        prefixSum = [nums[0]]
        for i in range(1, len(nums)):
            prefixSum.append(prefixSum[i-1]+nums[i])
        n = len(nums)-1
        for i in range(n+1):
            if prefixSum[n]-prefixSum[i]==(prefixSum[i-1] if i else 0):
                return i
        return -1
