class Solution:
    def minOperations(self, nums: list[int]) -> int:
        curr_max = nums[0]
        ans = 0
        increase = 0
        min_inv = -1
        
        for i in range(len(nums)):
            if nums[i]+increase<curr_max:
                ans += (curr_max - (nums[i]+increase))
                increase += curr_max-(nums[i]+increase)
                min_inv = min(min_inv, i)
            curr_max = max(curr_max, nums[i]+increase)

        return ans
