class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        n = len(nums)
        if n<3: return n
        ans = 2
        dp = [{} for _ in range(n)]

        for i in range(n):
            for j in range(i):
                diff = nums[i]-nums[j]
                dp[i][diff] = dp[j].get(diff, 1)+1
                if dp[i][diff]>ans: ans = dp[i][diff]

        return ans
