class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        nums.sort()
        nums.append(float("inf"))
        count = 0
        min_element = nums[0]

        for i in range(1, len(nums)):
            if nums[i]-min_element>k:
                count += 1
                min_element = nums[i]

        return count
    

    # using sorted set to find diff faster 
    # another approach can be to use binary_search biset left to find next partition point
    # def partitionArray(self, nums: List[int], k: int) -> int:
    #     if k == 0:
    #         return len(set(nums))
    #     nums = sorted(list(set(nums)))
    #     ans = 0
    #     prev = -1
    #     for num in nums:
    #         if num>prev:
    #             prev = num
    #             ans += 1
    #             prev += k
    #         else:
    #             continue
    #     return ans
