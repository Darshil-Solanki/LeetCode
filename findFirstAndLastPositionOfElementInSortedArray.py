class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        if not nums or target<nums[0] or target>nums[-1]:
            return [-1,-1]
        def firstOccurence():
            left, right = 0, n
            while left<right:
                mid = (left+right)//2
                if nums[mid]>=target:
                    right = mid
                else:
                    left = mid+1
            if left==n:
                return -1 if nums[left]!=target else  n
            if nums[left]==target:
                return left
            return -1
  
        def lastOccurence():
            left, right = 0, n
            while left<right:
                mid = (left+right)//2
                if nums[mid]>target:
                    right = mid
                else:
                    left = mid+1
            if left==0:
                return -1 if nums[left]!=target else left
            if nums[left-1]==target:
                return left-1
            return -1
        
        return [firstOccurence(), lastOccurence()]
