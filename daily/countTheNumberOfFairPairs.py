class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()
        ans = 0
        n = len(nums)

        def lower_bound(low, high, target):
            while low<=high:
                mid = (low+high)//2
                if target<=nums[mid]:
                    high = mid-1
                else:
                    low = mid+1
            return low

        for i, num in enumerate(nums):
            low = lower_bound(i+1, n-1, lower-num)
            high = lower_bound(i+1, n-1, upper-num+1)

            ans+= high-low

        return ans
