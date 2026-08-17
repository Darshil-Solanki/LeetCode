class Solution:
    def stoneGameV(self, stoneValue: List[int]) -> int:
        n = len(stoneValue)
        f = [[0] * n for _ in range(n)]
        maxl = [[0] * n for _ in range(n)]
        maxr = [[0] * n for _ in range(n)]

        for left in range(n-1, -1, -1):
            maxl[left][left] = maxr[left][left] = stoneValue[left]
            total = stoneValue[left]
            suml = 0
            i = left - 1
            for right in range(left + 1, n):
                total += stoneValue[right]
                while i + 1 < right and (suml + stoneValue[i + 1]) * 2 <= total:
                    suml += stoneValue[i + 1]
                    i += 1
                if left <= i:
                    f[left][right] = max(f[left][right], maxl[left][i])
                if i + 1 < right:
                    f[left][right] = max(f[left][right], maxr[i+2][right])
                if suml * 2 == total:
                    f[left][right] = max(f[left][right], maxr[i+1][right])
                maxl[left][right] = max( maxl[left][right-1], total + f[left][right] )

                maxr[left][right] = max( maxr[left+1][right], total + f[left][right])
        return f[0][n-1]

        # prefix = [0]
        # for stone in stoneValue:
        #     prefix.append(prefix[-1]+stone)

        # @lru_cache
        # def dp(left, right):
        #     if left == right:
        #         return 0

        #     total = prefix[right+1] - prefix[left]
        #     left_sum = ans = 0
        #     for i in range(left, right):
        #         left_sum += stoneValue[i]
        #         right_sum = total - left_sum
        #         if left_sum < right_sum:
        #             ans = max(ans, left_sum + dp(left, i))
        #         elif right_sum < left_sum:
        #             ans = max(ans, right_sum + dp(i+1, right))
        #         else:
        #             ans = max(ans, max(dp(left, i), dp(i+1, right)) + left_sum )
            
        #     return ans

        # return dp(0, len(stoneValue)-1)
