class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        prev = nums[0]
        p = q = len(nums)
        for i in range(1, len(nums)):
            if nums[i]>prev:
                prev = nums[i]
            else:
                p = i-1
                break
        
        if p==0 or p==len(nums): return False
        prev = nums[p]
        for i in range(p+1, len(nums)):
            if nums[i]<prev:
                prev = nums[i]
            else:
                q = i - 1
                break
        if q == p or q>=len(nums)-1: return False
        prev = nums[q]
        for i in range(q+1, len(nums)):
            if nums[i]>prev:
                prev = nums[i]
            else:
                return False
            
        return True   
