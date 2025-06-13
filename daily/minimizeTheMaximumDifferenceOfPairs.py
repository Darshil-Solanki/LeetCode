class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        nums.sort()
        n = len(nums)
        
        def check(thresold):
            i, count = 0, 0
            while i < n-1:
                if nums[i+1] - nums[i] <= thresold:
                    count += 1
                    i += 1
                i += 1

            return count>=p
                
        
        left, right = 0, nums[-1]-nums[0]
        while left<right:
            mid = (left+right)//2

            if check(mid):
                right = mid
            else:
                left = mid+1

        return left
