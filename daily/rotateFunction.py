class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        tot = sum(nums)
        f, n = sum(i*n for i, n in enumerate(nums)), len(nums)

        ans = f
        for i in range(n-1, 0, -1):
            f += tot-n*nums[i]
            ans = max(ans, f)
        
        return ans
