class Solution:
    def maxTotal(self, nums: List[int], s: str) -> int:
        n = len(nums)
        if s[0] == "1":
            prev0, prev1 = float("-inf"), nums[0]
        else:
            prev0, prev1 = 0, float("-inf")
        
        for i in range(1, n):
            if s[i] == "1":
                curr1 = max(prev0, prev1)+nums[i]
                curr0 = max(prev0+nums[i-1], prev1)
            else:
                curr0 = max(prev0, prev1)
                curr1 = float("-inf")
            prev0, prev1 = curr0, curr1

        return max(prev0, prev1)
