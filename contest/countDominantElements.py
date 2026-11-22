class Solution:
    def countDominantElements(self, nums: list[int]) -> int:
        ans = 0
        n = len(nums)
        if n==1:
            return 1
        for i, num in enumerate(nums):
            if i == 0:
                if num >= nums[1]:
                    ans += 1
            elif i == n-1:
                if num >= nums[-2]:
                    ans += 1
            else:
                if num >= (nums[i-1]+nums[i+1])/2:
                    ans += 1

        return ans
                
            
