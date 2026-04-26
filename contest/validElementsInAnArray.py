class Solution:
    def findValidElements(self, nums: list[int]) -> list[int]:
        temp = []
        n = len(nums)
        taken = [False]*n
        prev_max = 0
        for i, num in enumerate(nums):
            if num>prev_max:
                temp.append((i, num))
                prev_max = num
                taken[i] = True
        prev_max = 0
        for i in range(n-1, -1, -1):
            if nums[i]>prev_max and not taken[i]:
                temp.append((i, nums[i]))
            prev_max = max(nums[i], prev_max)

        temp.sort()
        return [num for i, num in temp]
            
