class Solution:
    def smallestBalancedIndex(self, nums: list[int]) -> int:
        # TLE contest code
        # prefix_sum = [0]
        # temp = 0
        # temp2 = 1
        # for num in nums:
        #     temp += num
        #     temp2 *= num
        #     prefix_sum.append(temp)
        
        # for i, num in enumerate(nums):
        #     temp2 //= num
        #     if prefix_sum[i] == temp2:
        #         return i
        # return -1
        
        # from contest solutions
        total = sum(nums)
        limit = total
        n = len(nums)
        rp = 1
        ans = -1
        for i in range(n-1, -1, -1):
            total -= nums[i]
            if total == rp:
                ans = i
            if rp>limit//nums[i]:
                rp = limit
            else:
                rp *= nums[i]
        return ans
