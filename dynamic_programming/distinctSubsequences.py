class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        self.ans = 0
        n = len(s)
        m = len(t)

        dp = [0]*(m+1)
        dp[0] = 1
        for i in range(n):
            for j in range(m-1, -1, -1):
                if s[i] == t[j]:
                    dp[j+1] += dp[j]
        
        return dp[m]

        # memo = {}
        # def dp(curr, i):
        #     if curr == t: return 1
        #     if i==n: return 0
        #     currState = str(i)+curr
        #     if currState in memo:
        #         return memo[currState]
        #     memo[currState] = dp(curr+s[i], i+1) + dp(curr, i+1)
        #     return memo[currState]
        # return dp("", 0)

        # from Submission
        # memo = {}
        # m, n = len(s), len(t)

        # def dp(i, j):
        #     if i == m or j == n or m - i < n - j:
        #         return int(j == len(t))
            
        #     if (i,j) in memo:
        #         return memo[i, j]
            
        #     ans = dp(i + 1, j)

        #     if s[i] == t[j]:
        #         ans += dp(i + 1, j + 1)
            
        #     memo[i,j] = ans
        #     return ans

        # return dp(0,0)
