class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_mask = int(log2(max(nums)))+1
        dp = [0]*(1<<max_mask)
        
        for num in nums:
            dp[num] = num
        
        for i in range(1<<max_mask):
            if dp[i]:
                continue
            for m in range(max_mask):
                if i &(1<<m):
                    if dp[i^(1<<m)] > dp[i]:
                        dp[i] = dp[i^(1<<m)]
        
        all_set_bit = (1<<max_mask)-1
        return max(num*dp[all_set_bit^num] for num in nums)

        # ans = 0
        # nums_set = set(nums)
        # nums = list(nums_set)
        
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if nums[i] & nums[j] == 0:
        #             ans = max(ans, nums[i]*nums[j])
        
        # return ans
