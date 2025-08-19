class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        left, ans = 0, 0

        for right, num in enumerate(nums):
            if num==0:
                ans += right-left+1
            else:
                left = right + 1

        return ans
