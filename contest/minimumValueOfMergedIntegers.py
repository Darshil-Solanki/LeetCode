class Solution:
    def minMergedInteger(self, nums: list[int]) -> int:
        ans = float("inf")
        
        for i in range(0, len(nums), 2):
            a, b = nums[i], nums[i+1]
            ans = min(ans, int(str(a)+str(b)))

        return ans
