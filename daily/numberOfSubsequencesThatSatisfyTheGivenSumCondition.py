MOD = 1_000_000_007
class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        ans = 0

        left, right = 0, len(nums)-1
        while left<=right:
            if nums[left]+nums[right]<=target:
                n = right-left
                ans =  (ans + pow(2, n, MOD)) % MOD
                left += 1
            else:
                right -= 1
        
        return ans
