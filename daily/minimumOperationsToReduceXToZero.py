class Solution:
    def minOperations(self, nums: list[int], x: int) -> int:
        s = sum(nums)
        n = len(nums)
        left, curr, ans = 0, 0, -1
        k = s-x
        if x>s:
            return -1

        for right, num in enumerate(nums):
            curr += num
            
            while curr>k:
                curr -= nums[left]
                left += 1
            
            if curr==k:
                ans = max(ans, right-left+1)
        
        return -1 if ans == -1 else n - ans
