class Solution:
    def maxPairStrength(self, nums: list[int]) -> int:
        n = len(nums)
        ans = 0
        for i in range(n):
            a = nums[i]
            for j in range(i+1, n):
                if i != j:
                    ans = max(ans, (a * nums[j]) / gcd(a, nums[j])**2 )
        return int(ans)
