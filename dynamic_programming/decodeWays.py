class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        next, next1, next2 = 0, 1, 0  
        for i in range(n-1, -1, -1):
            curr = int(s[i])
            if not curr:
                next1, next2 = 0, next1
                continue
            if curr < 3 and i+1 < n and (curr*10 + int(s[i+1])) < 27:
                next = next1 + next2
            else:
                next = next1
            next, next1, next2 = 0, next, next1
        return next1

        # dp = [0]*(n+1)
        # dp[n]=1
        # for i in range(n-1, -1, -1):
        #     curr = int(s[i])
        #     if not curr:
        #         dp[i]=0
        #         continue
        #     if curr<3 and i+1<n and curr*10+int(s[i+1])<27:
        #         dp[i]=dp[i+1]+dp[i+2]
        #     else:
        #         dp[i] = dp[i+1]
        # return dp[0]

        # @cache
        # def dp(i):
        #     if i==n: return 1
            
        #     curr = int(s[i]) 
        #     if not curr: return 0

        #     if curr<3 and i+1<n and curr*10+int(s[i+1])<27:
        #         return dp(i+1)+dp(i+2)
        #     return dp(i+1)

        # return dp(0)
