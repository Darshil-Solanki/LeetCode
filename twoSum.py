class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n=len(nums)
        for i in range(n):
            for j in range(i+1, n):
                if nums[i]+nums[j]==target:
                    return [i,j]

# Better improveent using hashMap of Complement for sum problem
# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         mapSum = {}
#         for i in range(len(nums)):
#             compliment = target - nums[i]
#             if compliment in mapSum:
#                 return[i,mapSum[compliment]]
#             mapSum[nums[i]] = i
