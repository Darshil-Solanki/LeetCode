class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [0]*(target+1)
        dp[0] = 1

        for t in range(1, target+1):
            for n in nums:
                if t-n>=0:
                    dp[t]+=dp[t-n]
        
        return dp[target]
        
        # @cache
        # def dp(target):
        #     if target==0: return 1
        #     if target<0: return 0

        #     ans = 0
        #     for n in nums:
        #         ans+=dp(target-n)
            
        #     return ans
        
        # return dp(target)
