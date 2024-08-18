class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        L=0
        R=len(nums)-1
        while L<R:
            tot=nums[L]+nums[R]
            if tot==target:
                return [L+1,R+1]
            if tot<target:
                L+=1
            else:
                R-=1
