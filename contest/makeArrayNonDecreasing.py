class Solution:
    def maximumPossibleSize(self, nums: List[int]) -> int:
        ans = 1
        last_smallest = nums[0]
        
        for i in range(1, len(nums)):
            if nums[i]<last_smallest:
                continue
            elif nums[i]==last_smallest:
                ans+=1
            else:
                ans += 1
                last_smallest = nums[i]
                
        return ans
