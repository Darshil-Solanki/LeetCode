class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        nums.sort()
        prev = nums[0]
        ans = []
        
        for i in range(1, len(nums)):
            curr = nums[i]
            if curr>prev+1:
                ans.extend(list(range(prev+1, curr)))
            prev = curr
            
        return ans
