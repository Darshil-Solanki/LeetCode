class Solution:
    def countGoodRotations(self, nums: list[int]) -> int:
        n = len(nums)
        prefix_sum = [0]
        for num in nums:
            prefix_sum.append(prefix_sum[-1]+num)

        total = prefix_sum[-1]
        ans = 0
        for i in range(n):
            left = 0
            if i>n//2:
                left = total-prefix_sum[i] + prefix_sum[(n//2)-(n-i)]
            else:
                left = prefix_sum[i+n//2]-prefix_sum[i]
            right = total-left
            if left>right:
                ans += 1

        return ans
