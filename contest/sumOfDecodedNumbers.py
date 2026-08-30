class Solution:
    def sumDecoded(self, nums: list[int]) -> int:
        MOD = 1_000_000_007
        ans = 0

        def get_x_y(w, d):
            sd = str(d)
            return (int(sd[:w]), int(sd[w:]))
        
        for num in nums:
            w, d = num%10, num//10
            x, y = get_x_y(w, d)
            val = pow(x, y, MOD)
            ans = (ans + val) % MOD

        return ans
