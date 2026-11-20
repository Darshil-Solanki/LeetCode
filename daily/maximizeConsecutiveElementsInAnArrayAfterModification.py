class Solution:
    def maxSelectedElements(self, nums: List[int]) -> int:
        nums.sort()
        dp = defaultdict(int)
        ans = 0

        for num in nums:
            dp[num+1] = max(dp[num+1], dp[num]+1)
            dp[num] = max(dp[num], dp[num-1]+1)
            ans = max(ans, dp[num], dp[num+1])
        
        return ans
