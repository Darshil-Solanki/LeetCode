class Solution:
    def maxIncreasingSubarrays(self, nums: List[int]) -> int:
        dp = [1]*len(nums)

        for i in range(1, len(nums)):
            if nums[i]>nums[i-1]:
                dp[i]=dp[i-1]+1
        

        def check(k):
            for i in range(k-1, len(nums)-k):
                if dp[i]>=k and dp[i+k]>=k:
                    return True
            return False


        ans = 1
        left, right = 1, len(nums)//2

        while left<=right:
            mid = (left+right)//2
            if check(mid):
                ans = mid
                left = mid+1
            else:
                right = mid-1
        
        return ans

# O(n) faster approach
# class Solution:
#     def maxIncreasingSubarrays(self, nums: List[int]) -> int:
#         last_inc_len = 1
#         cur_inc_len = 1
#         ans = 1

#         last = nums[0]
#         for n in nums:
#             if n > last:
#                 cur_inc_len += 1
#             else:
#                 ans = max(ans, min(last_inc_len, cur_inc_len), cur_inc_len // 2)
#                 last_inc_len = cur_inc_len
#                 cur_inc_len = 1
#             last = n
#         return max(ans, min(last_inc_len, cur_inc_len), cur_inc_len // 2)
