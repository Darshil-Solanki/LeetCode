class Solution:
    def minInsertions(self, s: str) -> int:
        revs = s[::-1]
        if s==revs: return 0
        n = len(s)
        prev, curr = [0]*(n+1), [0]*(n+1)

        for i in range(1, n+1):
            for j in range(1, n+1):
                if revs[i-1]==s[j-1]:
                    curr[j] = 1+prev[j-1]
                else:
                    curr[j] = max(curr[j-1], prev[j])
            prev = curr[:]

        return len(s)-curr[n]  
