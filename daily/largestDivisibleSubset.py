class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        n = len(nums)

        dp = [1]*n

        max_size = 1
        max_index = 0

        for i in range(1, n):
            for j in range(i):
                if nums[i]%nums[j]==0:
                    if dp[j]+1>dp[i]:
                        dp[i]=dp[j]+1
            
            if dp[i]>max_size:
                max_size = dp[i]
                max_index = i
        
        result = []
        curr_num = nums[max_index]
        curr_size = max_size
        for i in range(max_index, -1, -1):
            if dp[i]==curr_size and curr_num % nums[i]==0:
                result.append(nums[i])
                curr_num = nums[i]
                curr_size -= 1

        result.reverse()
        return result
