class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        for i in range(n):
            if nums[i] in nums[i+1:i+k+1]:
                return True
        return False

# Solution from best runtimes
# class Solution:
#     def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
#         num_map = {}
#         for idx, value in enumerate(nums):
#             if value in num_map.keys():
#                 # check if it is within k distance
#                 if idx - num_map[value] <= k:
#                     return True
#             # otherwise update with new index to minimize distance
#             num_map[value] = idx
#         return False
