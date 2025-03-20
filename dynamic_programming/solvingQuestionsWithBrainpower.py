class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)
        dp = [0]*(n+1)

        for i in range(n-1, -1, -1):
            solve = questions[i][0]+(dp[i+questions[i][1]+1] if i+questions[i][1]+1<n else 0)
            not_solve = dp[i+1]
            dp[i] = max(solve, not_solve)
        
        return dp[0]

        # @cache
        # def dp(i):
        #     if i>=n: return 0
            
        #     solve = questions[i][0]+dp(i+questions[i][1]+1)
        #     not_solve = dp(i+1)
        #     return max(solve, not_solve)
        
        # return dp(0)
