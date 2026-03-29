class Solution:
    def minAbsoluteDifference(self, nums: list[int]) -> int:
        ans = float("inf")
        
        for i in range(len(nums)):
            num1 = nums[i]
            for j in range(len(nums)):
                if num1==1 and nums[j]==2:
                    ans = min(ans, abs(j-i))
                    
        return ans if ans != float("inf") else -1
