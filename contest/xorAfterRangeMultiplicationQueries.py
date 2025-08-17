class Solution:
    def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:
        MOD = 1_000_000_007
        for left, right, k, v in queries:
            for i in range(left, right+1, k):
                nums[i] = (nums[i]*v)%MOD
        
        ans = 0
        for n in nums:
            ans ^= n
        
        return ans
