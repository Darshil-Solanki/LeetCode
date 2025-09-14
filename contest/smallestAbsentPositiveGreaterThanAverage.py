class Solution:
    def smallestAbsent(self, nums: List[int]) -> int:
        nums.sort()
        max_num = nums[-1]
        if max_num<1:
            return 1
        def find(target):
            left, right = 0, len(nums)
            while left<=right:
                mid = (left+right)//2
                if nums[mid]==target:
                    return mid
                elif target<nums[mid]:
                    right = mid-1
                else:
                    left = mid+1
            return -1
            
        avg = floor((sum(nums)/len(nums))+1)
        
        for i in range(max(1, avg), max_num+1):
            if find(i)==-1:
                return i
        return max_num+1
