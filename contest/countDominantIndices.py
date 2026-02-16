class Solution:
    def dominantIndices(self, nums: List[int]) -> int:
        n = len(nums)
        prefix_sum = []
        temp = 0
        for num in nums:
            temp += num
            prefix_sum.append(temp)

        return sum(1 for i in range(n-1) if nums[i] > ((prefix_sum[n-1]-prefix_sum[i])/(n-i-1)))
