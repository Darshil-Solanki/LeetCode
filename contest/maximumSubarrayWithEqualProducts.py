class Solution:
    def maxLength(self, nums: List[int]) -> int:
        ans = 0
        for i in range(len(nums)):
            curr_prod = 1
            curr_gcd = curr_lcm = nums[i]
            for j in range(i, len(nums)):
                curr_prod *= nums[j]
                curr_gcd = gcd(curr_gcd, nums[j])
                curr_lcm = lcm(curr_lcm, nums[j])
                if curr_prod==(curr_gcd*curr_lcm) and j-i+1>ans:
                    ans = j-i+1
        return ans
