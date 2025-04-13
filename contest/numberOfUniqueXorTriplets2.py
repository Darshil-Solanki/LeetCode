class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        n = len(nums)
        if n==1 or n==2: return n
        uniqueXor = set()
        for i in range(n):
            for j in range(i+1, n):
                uniqueXor.add(nums[i]^nums[j])
        
        tripletXor = set()
        for x in uniqueXor:
            for num in nums:
                tripletXor.add(num^x)
        
        return len(tripletXor)
