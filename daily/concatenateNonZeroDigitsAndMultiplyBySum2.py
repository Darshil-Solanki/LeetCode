MOD = 1_000_000_007
pow10 = [1]*100_001
for i in range(1, 100001):
    pow10[i] = pow10[i-1] * 10 % MOD

class Solution:
    def sumAndMultiply(self, s: str, queries: List[List[int]]) -> List[int]:
        n = len(s)
        prefix_arr = [[0, 0, 0] for _ in range(n+1)] # prefix[i] prefix of [num, digit_sum, length]

        for i, c in enumerate(s):
            d = int(c)
            prefix_arr[i+1][0] = (prefix_arr[i][0]*10+d)%MOD if d>0 else prefix_arr[i][0]
            prefix_arr[i+1][1] = prefix_arr[i][1] + d
            prefix_arr[i+1][2] = prefix_arr[i][2] + (d>0)
        
        ans = []
        for l, r in queries:
            length = prefix_arr[r+1][2] - prefix_arr[l][2]
            digit_sum = prefix_arr[r+1][1] - prefix_arr[l][1]
            num = prefix_arr[r+1][0] - prefix_arr[l][0] * pow10[length]
            ans.append((num * digit_sum) % MOD)
        
        return ans
