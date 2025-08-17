class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        dp = [0]*(n+1)
        dp[0] = 1
        if k==0:
            return 1
        temp_sum = 1

        for i in range(1, n+1):
            dp[i] = temp_sum / maxPts
            if i<k:
                temp_sum += dp[i]
            if i-maxPts > -1 and i-maxPts<k:
                temp_sum -= dp[i-maxPts]
        
        return sum(dp[k:])
