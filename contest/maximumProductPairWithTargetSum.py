class Solution:
    def maxProductPair(self, nums: list[int], target: int) -> list[int]:
        n = len(nums)
        max_prod = float("-inf")
        ans = [-1, -1]
        
        for i in range(n):
            for j in range(n):
                if i == j or nums[i]<=nums[j] or nums[i]+nums[j]!=target:
                    continue
                curr_prod = nums[i]*nums[j]
                if curr_prod  > max_prod:
                    max_prod = curr_prod
                    ans = [i, j]

        return ans
