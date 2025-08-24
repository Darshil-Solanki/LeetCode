class Solution:
    def maxValue(self, nums: List[int]) -> List[int]:
        n = len(nums)
        if not n: return nums

        max_l_prefix = []
        max_n = 0
        for num in nums:
            max_n = max(max_n, num)
            max_l_prefix.append(max_n)

        min_r_prefix = [0]*n
        min_r_prefix[n-1] = nums[n-1]
        for i in range(n-2, -1, -1):
            min_r_prefix[i] = min(nums[i], min_r_prefix[i+1])

        nums[n-1] = max_l_prefix[n-1]
        for i in range(n-2, -1, -1):
            nums[i] = max_l_prefix[i]
            if max_l_prefix[i]>min_r_prefix[i+1]:
                nums[i] = nums[i+1]
                
        return nums
