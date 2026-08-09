class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        memo = [[0] * len(piles) for _ in range(len(piles))]
        suffix_sum = piles[:]
        n = len(piles)

        for i in range(len(suffix_sum)-2, -1, -1):
            suffix_sum[i] += suffix_sum[i+1]
        
        def dp(max_till_now, curr_idx):
            if curr_idx + 2 * max_till_now >= n:
                return suffix_sum[curr_idx]
            
            if memo[curr_idx][max_till_now]:
                return memo[curr_idx][max_till_now]
            
            ans = float("inf")

            for i in range(1, 2 * max_till_now+1):
                ans = min(ans, dp(max(i, max_till_now), curr_idx+i))

            memo[curr_idx][max_till_now] = suffix_sum[curr_idx] - ans
            return memo[curr_idx][max_till_now]


        return dp(1, 0)
