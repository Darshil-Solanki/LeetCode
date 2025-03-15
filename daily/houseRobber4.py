class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        n = len(nums)

        def check(capability):
            robbed = i = 0
            while i<n:
                if nums[i]>capability:
                    i+=1
                    continue
                robbed+=1
                i+=2
            return robbed>=k

        left, right = 1, max(nums)
        while left<right:
            mid = (left+right)//2
            if check(mid):
                right = mid
            else:
                left = mid+1
        return left
