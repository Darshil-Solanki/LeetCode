class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        neg = pos = 0
        for n in nums:
            if n<0:
                neg+=1
            elif n>0:
                pos+=1
        return max(neg, pos)
        
        # left, right = 0, len(nums)-1
        # while left<=right:
        #     mid = (left+right)//2
        #     if nums[mid]>=0:
        #         right=mid-1
        #     else:
        #         left=mid+1
        # negIdx = left

        # left, right = 0, len(nums)-1
        # while left<=right:
        #     mid = (left+right)//2
        #     if nums[mid]>0:
        #         right=mid-1
        #     else:
        #         left=mid+1
        # posIdx = left
        
        # return max(len(nums)-posIdx, negIdx) 
