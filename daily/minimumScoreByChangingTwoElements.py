class Solution:
    def minimizeSum(self, nums: List[int]) -> int:
        mn_a = mn_b = mn_c = float("inf")
        mx_a = mx_b = mx_c = float("-inf")
        n = len(nums)
        if n == 3:
            return 0

        for num in nums:
            if num > mx_a:
                mx_a, mx_b, mx_c = num, mx_a, mx_b
            elif num > mx_b:
                mx_b, mx_c = num, mx_b
            elif num > mx_c:
                mx_c = num

            if num < mn_a:
                mn_a, mn_b, mn_c = num, mn_a, mn_b
            elif num < mn_b:
                mn_b, mn_c = num, mn_b
            elif num < mn_c:
                mn_c = num
            

        largest_removal = mx_c - mn_a
        minimum_removal = mx_a - mn_c
        minmax_removal = mx_b - mn_b

        return min(largest_removal, minimum_removal, minmax_removal)
