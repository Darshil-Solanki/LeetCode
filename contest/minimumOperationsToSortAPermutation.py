class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0
        
        fwd = sum((nums[i] - nums[i-1]) % n == 1 for i in range(n))
        rev = sum((nums[i] - nums[i-1]) % n == n - 1 for i in range(n))
        
        idx = nums.index(0)
        
        if fwd == n:
            return 0 if not idx else min(idx, n - idx + 2)
            
        if rev == n:
            return min(idx + 2, n - idx)
            
        return -1
