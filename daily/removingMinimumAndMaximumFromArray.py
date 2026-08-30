class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        n = len(nums)
        mn, mn_i, mx, mx_i = float("inf"), -1, float("-inf"), -1
        for i, num in enumerate(nums):
            if num<mn:
                mn, mn_i = num, i
            if num>mx:
                mx, mx_i = num, i
        
        ans1 = max(mn_i, mx_i) + 1
        ans2 = n - min(mn_i, mx_i)
        ans3 = min(mn_i, mx_i) + 1 + n - max(mn_i, mx_i)
        return min(ans1, ans2, ans3)
