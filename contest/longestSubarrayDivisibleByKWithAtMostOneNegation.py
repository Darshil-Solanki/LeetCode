class Solution:
    def longestSubarray(self, nums: list[int], k: int) -> int:
        ans = 0
        n = len(nums)
        for i, num in enumerate(nums):
            total = 0
            doubled = set() # 2x % k
            for j in range(i, n):
                total += nums[j]
                doubled.add((2*nums[j]) % k)
                remainder = total % k
                if remainder == 0 or remainder in doubled:
                    ans = max(ans, j-i+1)

        return ans
