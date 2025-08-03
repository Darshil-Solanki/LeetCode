class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        ans = n-1
              
        for i, num in enumerate(nums):
            ans = min(ans, i+n-bisect_right(nums, num*k))

        return ans
