class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        n = len(pairs)
        dp = [1]*n
        pairs.sort(key = lambda x: x[1])
        for i in range(n-1, -1, -1):
            for j in range(i+1, n):
                if pairs[i][1]<pairs[j][0]:
                    dp[i] = max(dp[i], dp[j]+1)

        return max(dp)

        # pairs.sort(key = lambda x: x[1])
        # endLink = pairs[0][1]
        # cnt = 1
        # for start, end in pairs:
        #     cnt += endLink < start
        #     endLink = end if endLink < start else endLink
        # return cnt
