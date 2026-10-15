class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0

        for i in range(n):
            curr_set = set()
            for j in range(i, n):
                curr_set.add(nums[j])
                ans += len(curr_set)**2
        
        return ans
