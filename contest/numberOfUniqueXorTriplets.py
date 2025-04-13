class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        n = len(nums)
        if n==1: return 1
        if n==2: return 2
        return (2**floor(log(n,2)))*2
