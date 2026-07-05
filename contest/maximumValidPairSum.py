class Solution:
    def maxValidPairSum(self, nums: list[int], k: int) -> int:
        n = len(nums)
        max_num = [0]*n
        
        for i in range(n-2, -1, -1):
            max_num[i] = max(max_num[i+1], nums[i+1])

        ans = 0
        for i in range(n-k):
            ans = max(nums[i]+max_num[i+k-1], ans)

        return ans
