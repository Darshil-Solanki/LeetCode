class Solution:
    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        n = len(nums)

        dp = [[-1]*2 for _ in range(n+1)]
        dp[n] = [-float("inf"), 0]

        for node in range(n-1, -1, -1):
            for c in range(2):
                noXorDone = nums[node] + dp[node+1][c]
                XorDone = (nums[node]^k) + dp[node+1][c^1]
                dp[node][c] = max(noXorDone, XorDone)
            
        return dp[0][1]
