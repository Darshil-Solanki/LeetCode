class Solution:
    def maximumTotalDamage(self, power: List[int]) -> int:
        u_power = list(Counter(power).items())
        u_power.sort(key=lambda x: x[0])
        n = len(u_power)
        dp =  [0]*n
        j, mx = 0, 0
        
        for i in range(n):          
            while j<i and u_power[j][0] < u_power[i][0]-2:
                mx = max(mx, dp[j])
                j += 1
            
            dp[i] = mx + u_power[i][0]*u_power[i][1]
        return max(dp)


        # @cache
        # def dp(i, skip):
        #     if i==n:
        #         return 0

        #     use = cnt[u_power[i]]*u_power[i] + dp(i+1, u_power[i]+2) if u_power[i]>skip else 0
        #     not_use = dp(i+1, skip)
        #     return max(use, not_use)
        
        # return dp(0, 0)
