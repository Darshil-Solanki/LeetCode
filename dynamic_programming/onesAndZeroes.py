class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        length = len(strs)
        
        @cache
        def dp(i, zero, one):
            if i==length: return 0

            curr_zero, curr_one = strs[i].count("0"), strs[i].count("1")
            pick = 0
            if curr_zero<=zero and curr_one<=one:
                pick = 1+dp(i+1, zero-curr_zero, one-curr_one)
            not_pick = dp(i+1, zero, one)
            return max(pick, not_pick)

        return dp(0, m, n)

'''
    capacity = [5,3] (5 zeroes, 3 ones)

    0/1 knapsack:
    strs = [[1,1], [3,1], [2,4], [0,1], [1,0]]
    Either we include strs[i] or exclude
        If we include:
        dp[1,j] = dp[0,j] or dp[]
    0   0 -inf -inf -inf
    1   0 -inf -inf -inf
    2
    3
    4
    5

    dp[0][0][0] = 0
    dp[i][j][k] = dp[i-1][j][k] (skip)
    if dp[i-1][j-strs[i][0]][k-strs[i][1]] >= 0:
        dp[i][j][k] = dp[i-1][j-strs[i][0]][k-strs[i][1]] + 1
'''

# class Solution:
#     def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
#         s = len(strs)
#         arr = []
#         for x in strs:
#             nZeroes, nOnes = 0,0
#             for i in x:
#                 if i == '0':
#                     nZeroes += 1
#                 elif i == '1':
#                     nOnes += 1
#             arr.append([nZeroes, nOnes])

#         dp = [[0 for _ in range(n+1)] for _ in range(m+1)]

#         for nZeroes, nOnes in arr:
#             for i in range(m, nZeroes - 1, -1):
#                 for j in range(n, nOnes - 1, -1):
#                     dp[i][j] = max(dp[i][j], dp[i-nZeroes][j-nOnes] + 1)
#         return dp[m][n]
