class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        n = len(days)
        lastday = days[-1]
        travel_day = set(days)
        dp = [0]*(lastday+1)

        for day in range(1, lastday+1):
            if day not in travel_day:
                dp[day] = dp[day-1]
            else:
                cost1 = dp[day-1]+costs[0]
                cost7 = dp[max(0, day-7)]+costs[1]
                cost30 = dp[max(0, day-30)]+costs[2]
                
                dp[day] = min(cost1, cost7, cost30)

        return dp[lastday]


        # @cache
        # def dp(i, till):
        #     if i==n or till>=365: return 0
        #     if days[i]<=till: return dp(i+1, till)

        #     day1 = costs[0]+dp(i+1, days[i])
        #     day7 = costs[1]+dp(i+1, days[i]+6)
        #     day30 = costs[2]+dp(i+1, days[i]+29)
            
        #     return min(day1, day7, day30)
        
        # return dp(0, 0)
