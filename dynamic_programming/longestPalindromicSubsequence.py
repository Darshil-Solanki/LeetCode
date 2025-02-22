class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        prev, curr = [0]*n, [0]*n
        for i in range(n-1, -1, -1):
            curr[i] = 1
            for j in range(i+1, n):
                if s[i]==s[j]:
                    curr[j] = prev[j-1]+2
                else:
                    curr[j] = max(prev[j], curr[j-1])
            prev = curr[:]
        return curr[n-1]
        

        # def dp(start, end):
        #     if start == end: return 1
        #     if start>end: return 0
        #     if (s[start]==s[end]): return 2+dp(start+1, end-1)
        #     left = dp(start+1, end)
        #     right = dp(start, end-1)
        #     return max(left, right)
        # return dp(0, len(s)-1)
