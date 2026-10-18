class Solution:
    def numOfWays(self, nums: list[int]) -> int:
        MOD = 1_000_000_007

        def dfs(nums):
            n = len(nums)
            if n < 3:
                return 1
            
            left_nodes = [a for a in nums if a < nums[0]]
            right_nodes = [b for b in nums if b > nums[0]]
            
            return dfs(left_nodes) * dfs(right_nodes) * comb(n-1, len(left_nodes))
        
        return (dfs(nums) - 1) % MOD
