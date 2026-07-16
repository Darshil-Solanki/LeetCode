class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        mx = nums[0]
        prefix_gcd = []
        
        for num in nums:
            mx = max(num, mx)
            prefix_gcd.append(gcd(mx, num))
        
        prefix_gcd.sort()
        tot = 0
        n = len(prefix_gcd)
        for i in range(n//2):
            tot += gcd(prefix_gcd[i], prefix_gcd[n-i-1])
        return tot
