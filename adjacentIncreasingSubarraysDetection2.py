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
