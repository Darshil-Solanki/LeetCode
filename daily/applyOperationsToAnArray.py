class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        ans = []
        for i in range(len(nums)-1):
            if nums[i]==nums[i+1]:
                nums[i]*=2
                nums[i+1]=0
            if nums[i]:
                ans.append(nums[i])
        if nums[-1]: ans.append(nums[-1])
        ans.extend([0]*(len(nums)-len(ans)))
        return ans
