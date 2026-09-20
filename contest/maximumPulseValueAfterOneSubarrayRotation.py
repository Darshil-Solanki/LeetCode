class Solution:
    def maxValue(self, nums: List[int]) -> int:
        max_delta = prefix_sum = 0
        max_sum_odd, max_sum_even = 0, float("-inf")

        for i, num in enumerate(nums):
            if i % 2 == 0:
                prefix_sum += num
                if i>0:
                    curr_delta = 2 * (max_sum_even - prefix_sum)
                    if curr_delta > max_delta:
                        max_delta = curr_delta
                if prefix_sum > max_sum_even:
                    max_sum_even = prefix_sum
            else:
                prefix_sum -= num
                curr_delta = 2 * (max_sum_odd - prefix_sum)
                if curr_delta > max_delta:
                    max_delta = curr_delta
                if prefix_sum > max_sum_odd:
                    max_sum_odd = prefix_sum
        
        return prefix_sum + max_delta
