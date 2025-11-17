class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        try:
            prev = nums.index(1)
        except:
            return True
        n = len(nums)

        for i in range(prev+1, n):
            if nums[i]:
                if i-prev>k:
                    prev = i
                    continue
                return False
        
        return True
