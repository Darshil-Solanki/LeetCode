class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        tot = sum(nums)
        if tot % 2 != 0: return False
        target = tot // 2
        n = len(nums)
        
        dp = [False] * (target + 1)
        dp[0] = True 

        for num in nums:
            for j in range(target, num - 1, -1):
                dp[j] = dp[j] or dp[j - num]

        return dp[target]
    
        # recursive solution
        # tot = sum(nums)
        # if tot%2: return False
        # target = tot//2
        # n = len(nums)
        
        # @cache
        # def dp(i, sm):
        #     if i==n:
        #         if sm==target:
        #             return True
        #         return False
        #     if sm>target: return False

        #     ans = False
        #     for j in range(i, n):
        #         ans|=dp(j+1, sm+nums[j])

        #     return ans

        # return dp(0,0)
