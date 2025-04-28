class Solution:
    def isGoodArray(self, nums: List[int]) -> bool:
        # Bezout's identity ax+by=d if gcd(a, b) = d
        if len(nums)==1: return nums[0]==1

        a = nums[0]
        for i in range(1, len(nums)):
            if gcd(a, nums[i])==1:
                return True
            a = gcd(a, nums[i])
        
        return False
