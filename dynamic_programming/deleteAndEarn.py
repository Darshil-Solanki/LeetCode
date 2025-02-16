class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        mx = max(nums)+1
        points = [0]*mx

        for n in nums:
            points[n]+=n

        prev = curr = 0
        for value in points:
            prev, curr = curr, max(prev+value, curr)

        return curr
