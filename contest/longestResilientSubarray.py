class Solution:
    def resilientSubarray(self, nums: list[int], k: int) -> int:
        ans = i = 0

        while i < len(nums):
            r = nums[i] % k
            j = i + 1

            while j < len(nums) and nums[j] % k == r:
                j += 1

            curr_length = j - i
            period = k // gcd(r, k)
            valid_length = 1 + ((curr_length - 1) // period) * period
            ans = max(ans, valid_length)

            i = j
            
        return ans
