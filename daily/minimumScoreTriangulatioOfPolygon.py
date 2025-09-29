class Solution:
    def minScoreTriangulation(self, values: List[int]) -> int:
        @lru_cache(None)
        def dp(i, j):
            if i+2>j:
                return 0
            if i+2 == j:
                return values[i] * values[i+1] * values[i+2]
            
            return min((values[i]*values[k]*values[j]+dp(i, k)+dp(k, j)) for k in range(i+1, j))

        return dp(0, len(values)-1)

        # iterative approach
        # n = len(A)
        # dp = [[0]*n for _ in range(n)]
        # for length in range(2,n):
        #     for i in range(n-length):
        #         j = i+length
        #         dp[i][j] = min(dp[i][k]+dp[k][j]+A[i]*A[k]*A[j] for k in range(i+1,j))
        # return dp[0][n-1]
