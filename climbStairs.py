class Solution:
    def climbStairs(self, n: int) -> int:
        if not n or n==1:
            return 1
        prev = curr = 1
        for i in range(2, n+1):
            temp = prev
            prev = curr
            curr = temp+curr
        return curr
    # DP
    #     dp = [0]*(n+1)
    #     dp[1]=dp[0]=1
    #     print(dp)
    #     for i in range(2,n+1):
    #         dp[i]=dp[i-1]+dp[i-2]
    #     return dp[n]

    # Memoization
    #     memo = {}
    #     return self.helper(n, memo)
    # def helper(self, n, memo):
    #     if not n or n==1:
    #         return 1
    #     if n not in memo:
    #         memo[n] = self.helper(n-1, memo)+self.helper(n-2, memo)
    #     return memo[n]
