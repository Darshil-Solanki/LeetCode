class Solution:
    def countValidSubarrays(self, nums: list[int], x: int) -> int:
        n = len(nums)
        ans = 0
        x_str = str(x)

        @cache
        def valid(num):
            n_str = str(num)
            return n_str[0] == n_str[-1] == x_str
                
        for i in range(n):
            tot = 0
            for j in range(i, n):
                tot += nums[j]
                if valid(tot):
                    ans += 1
        return ans
