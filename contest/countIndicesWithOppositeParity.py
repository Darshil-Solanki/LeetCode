class Solution:
    def countOppositeParity(self, nums: list[int]) -> list[int]:
        ans = []
        for i, num in enumerate(nums):
            even_flag = 1 if num%2==0 else 0
            ans.append(sum(1 for j in range(i+1, len(nums)) if nums[j]%2==even_flag))
        return ans
