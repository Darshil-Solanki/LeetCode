class Solution:
    def findDisappearedNumbers(self, nums: list[int], lower: int, upper: int) -> list[list[int]]:
        nums.sort()
        ans = []
        curr = lower
        
        for num in nums:
            if num<lower:
                continue
            if num>upper:
                break
            if num>curr:
                ans.append([curr, num-1])
            curr = num + 1

        if curr<=upper:
            ans.append([curr, upper])

        return ans
