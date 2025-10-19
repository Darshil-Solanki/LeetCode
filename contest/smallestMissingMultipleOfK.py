class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        nums.sort()
        i = 1
        
        for n in nums:
            if n>i*k:
                return i*k
            elif n == i*k:
                i += 1

        return i*k
