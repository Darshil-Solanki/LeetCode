class Solution:
    def countElements(self, nums: List[int], k: int) -> int:
        nums.sort()
        ans = 0
        
        for n in nums:
            r = bisect_right(nums, n)
            if len(nums)-r>=k:
                ans += 1

        return ans
