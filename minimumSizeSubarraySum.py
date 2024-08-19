class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        if not n:
            return 0
        l=r=0
        tot=0
        mn=float("inf")
        while r<n and l<n:
            tot+=nums[r]
            while tot>=target and l<=r:
                mn = r-l+1 if r-l+1<mn else mn
                tot-=nums[l]
                if l!=r:
                    l+=1
            r+=1
        return mn if mn != float('inf') else 0

    # Better way 
    # def minSubArrayLen(self, target: int, nums: List[int]) -> int:
    #     n = len(nums)
    #     if not n:
    #         return 0 
    #     l = 0
    #     s = 0
    #     ans = float('inf')
    #     for r in range(n):
    #         s += nums[r]
    #         while s >= target:
    #             ans = min(ans, r-l+1)
    #             s -= nums[l]
    #             l += 1
    #     return ans if ans != float("inf") else 0
