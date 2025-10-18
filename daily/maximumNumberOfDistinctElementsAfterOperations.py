class Solution:
    def maxDistinctElements(self, nums: List[int], k: int) -> int:
        nums.sort()
        prev = nums[0]-k
        ans = 1
        
        for i in range(1, len(nums)):
            curr = min(max(nums[i]-k, prev+1), nums[i]+k)
            if curr>prev:
                ans +=1
            prev = curr

        return ans
