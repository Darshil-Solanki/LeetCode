class Solution:
    def subsequencePairCount(self, nums: List[int]) -> int:
        MOD = 1_000_000_007
        mx = max(nums)
        prev_dp = [[0] * (mx + 1) for _ in range(mx + 1)]
        prev_dp[0][0] = 1

        for num in nums:
            curr_dp = [[0] * (mx + 1) for _ in range(mx + 1)]

            for j in range(mx + 1):
                divisor1 = gcd(j, num)
                for k in range(mx + 1):
                    val = prev_dp[j][k]
                    if val == 0:
                        continue
                    
                    divisior2 = gcd(k, num)
                    curr_dp[j][k] = (curr_dp[j][k] + val) % MOD
                    curr_dp[divisor1][k] = (curr_dp[divisor1][k] + val) % MOD
                    curr_dp[j][divisior2] = (curr_dp[j][divisior2] + val) % MOD
            
            prev_dp = curr_dp
        
        ans = 0
        for j in range(1, mx+1):
            ans = (ans + curr_dp[j][j]) % MOD
        
        return ans
