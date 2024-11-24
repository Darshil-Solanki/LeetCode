class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        prefixSum = [nums[0]]
        for i in range(1, len(nums)):
            prefixSum.append(prefixSum[i-1]+nums[i])
        res = float("inf")
        for i, s in enumerate(prefixSum):
            for j in range(l, r+1):
                if i-j==-1 and s>0:
                    res = min(res, s)
                currSum = prefixSum[i-j]
                if i-j>-1 and s-currSum>0:
                    res = min(res, s-currSum)
        return -1 if res == float('inf') else res
