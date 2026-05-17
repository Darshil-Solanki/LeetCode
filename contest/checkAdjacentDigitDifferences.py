class Solution:
    def isAdjacentDiffAtMostTwo(self, s: str) -> bool:
        nums = list(map(int, list(s)))
        n = len(nums)
        for i in range(n-1):
            if abs(nums[i]-nums[i+1])>2:
                return False
        return True
