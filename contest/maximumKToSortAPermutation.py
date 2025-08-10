class Solution:
    def sortPermutation(self, nums: List[int]) -> int:
        ans = (1<<(len(nums)-1).bit_length())-1
        temp = ans

        for i, num in enumerate(nums):
            if num != i:
                ans &= num
        
        return 0 if ans==temp else ans
