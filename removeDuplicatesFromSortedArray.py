class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        li = 1
        prev = nums[0]
        for num in nums:
            if num!=prev:
                nums[li]=num
                li+=1
            prev = num
        return li
        
        
