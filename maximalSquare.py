class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m, n = len(matrix), len(matrix[0])
        maxS = 0
        dp = [[0]*(n+1) for i in range(m+1)]
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                if matrix[i][j]=="1":
                    if dp[i+1][j+1] and dp[i][j+1] and dp[i+1][j]:
                        dp[i][j]=1+min(dp[i+1][j+1], dp[i][j+1], dp[i+1][j])
                        if dp[i][j]>maxS:
                            maxS=dp[i][j]
                    else:
                        dp[i][j]=1
                        if not maxS:
                            maxS=1
        return maxS*maxS

    # More efficient code having one row at a time instead of dp grid
    # def maximalSquare(self, matrix: List[List[str]]) -> int:
    #     n, m = len(matrix), len(matrix[0])
    #     dp, size = [0] * m, 0
    #     for row in matrix:
    #         for i in range(m):
    #             if row[i] == '1':
    #                 dp[i] += 1
    #             else:
    #                 dp[i] = 0
    #         cnt = 0
    #         for x in dp:
    #             if x > size:
    #                 cnt += 1
    #             else:
    #                 cnt = 0
    #             if cnt == size + 1:
    #                 size += 1
    #                 break
    #     return size * size
