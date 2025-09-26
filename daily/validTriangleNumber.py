class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        ans = 0

        for i in range(len(nums) - 2):
            if not nums[i]:
                continue
            a = nums[i]
            k = i + 2
            for j in range(i + 1, len(nums) - 1):
                # right = bisect_left(nums, a+nums[j]) - j - 1
                # if right>0:
                #     ans += right
                while (k < len(nums)) and (a + nums[j] > nums[k]):
                    k += 1
                ans += k - j - 1

        return ans

# Reversing the strategy leads to nlogn solution
# class Solution:
#     def triangleNumber(self, nums: List[int]) -> int:
#         l = len(nums)
#         nums.sort()
#         result = 0
#         for i in range(l-1,1,-1):
#             target = nums[i]
#             m = 0
#             n = i -1
#             while m < n:
#                 if nums[m] + nums[n] <= target:
#                     m += 1
#                 else:
#                     result += n -m
#                     n -= 1
#         return result
