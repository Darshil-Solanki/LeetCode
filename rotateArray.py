class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if k==0:
            return nums
        temp = nums.copy()
        n = len(nums)
        for i in range(n):
            nums[i]=temp[(i+n-k)%n]
        return nums
