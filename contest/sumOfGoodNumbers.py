class Solution:
    def sumOfGoodNumbers(self, nums: List[int], k: int) -> int:
        length = len(nums)
        ans = 0
        for i, n in enumerate(nums):
            if (n>(nums[i-k] if (i-k)>-1 else float("-inf")) and n>(nums[i+k] if (i+k)<length else float("-inf"))):
               ans+=n  
        return ans
