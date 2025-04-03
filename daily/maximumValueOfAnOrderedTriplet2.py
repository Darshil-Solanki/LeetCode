class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        leftMaximum = [0]*len(nums)
        rightMaximum = [0]*len(nums)

        lmax = nums[0]
        for i in range(1, len(nums)-1):
            if lmax>nums[i-1]:
                leftMaximum[i] = lmax
            else:
                leftMaximum[i] = lmax = nums[i-1]
        
        rmax = nums[-1]
        for i in range(len(nums)-1-1, 0, -1):
            if rmax>nums[i+1]:
                rightMaximum[i] = rmax
            else:
                rightMaximum[i] = rmax = nums[i+1]
        
        ans = 0
        for j in range(1, len(nums)-1):
            ans = max(ans, (leftMaximum[j]-nums[j])*rightMaximum[j])
        
        return ans
