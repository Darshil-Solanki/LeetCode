class Solution:
    def countPartitions(self, nums: List[int], k: int) -> int:
        MOD = 1_000_000_007
        n = len(nums)
        dp, prefix = [0]*(n+1), [0]*(n+1)
        cnt = SortedList()
        
        dp[0]=1
        prefix[0] = 1

        j = 0
        for i in range(n):
            cnt.add(nums[i])
            while j<=i and cnt[-1] - cnt[0]>k:
                cnt.remove(nums[j])
                j += 1
            dp[i+1] = (prefix[i] - (prefix[j-1] if j>0 else 0)) % MOD
            prefix[i+1] = (prefix[i]+dp[i+1]) % MOD

        return dp[n]
