class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        min_arr = []
        mn = float("inf")
        for num in nums[::-1]:
            mn = min(num, mn)
            min_arr.append(mn)
        min_arr.reverse()
        mx = float("-inf")
        for i, num in enumerate(nums):
            mx, mn = max(mx, num), min_arr[i]
            if mx-mn<=k:
                return i
        return -1
