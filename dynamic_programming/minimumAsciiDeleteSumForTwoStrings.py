class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        m, n = len(s1), len(s2)
        prev, dp = [0], [0]*(n+1)
        for c in s2:
            prev.append(prev[-1]+ord(c))

        for i in range(1, m+1):
            dp[0] += ord(s1[i-1])
            for j in range(1, n+1):
                if s1[i-1] == s2[j-1]:
                    dp[j] = prev[j-1]
                else:
                    dp[j] = min(prev[j]+ord(s1[i-1]), dp[j-1]+ord(s2[j-1]))
            prev = dp[:]

        return dp[n]
