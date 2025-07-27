class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        count = 0
        n = len(nums)
        i = 1
        while i<n and nums[i] == nums[i-1]:
            i+=1
        if i==n: return 0
        
        prev = nums[i-1]
        flag = nums[i]>prev 
        j = i
        while j<n:
            if nums[j]>prev:
                while j<n and nums[j]>=prev:
                    prev = nums[j]
                    j+=1
                if j<n:
                    count +=1
            elif nums[j]<prev:
                while j<n and nums[j]<=prev:
                    prev = nums[j]
                    j+=1
                if j<n:
                    count+=1
        
        return count
            
            
