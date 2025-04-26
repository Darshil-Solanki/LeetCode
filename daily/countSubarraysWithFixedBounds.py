class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        # copied from submision
        left = ans = 0
        maxK_i = minK_i = -1

        for right, num in enumerate(nums):
            if num<minK or num>maxK:
                left = right+1
            
            if num==maxK: maxK_i=right
            if num==minK: minK_i=right
        
            ans += max(0, min(maxK_i, minK_i)-left+1)
        
        return ans
