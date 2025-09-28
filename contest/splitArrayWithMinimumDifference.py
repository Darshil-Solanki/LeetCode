class Solution:
    def splitArray(self, nums: List[int]) -> int:
        prefix_sum = []
        prev = temp = 0
        for num in nums:
            temp += num
            prefix_sum.append(temp)

        left_i, right_i = len(nums)-1, 0
        for i, n in enumerate(nums):
            if n>prev:
                prev = n
                continue
            left_i = i-1
            break
            
        prev = 0
        for i in range(len(nums)-1, -1, -1):
            n = nums[i]
            if n>prev:
                prev = n
                continue
            right_i = i+1
            break
        if left_i<right_i-1: return -1
        one, two  = float("inf"), float("inf")
        if left_i == right_i == 0:
            one = abs(nums[0] - (prefix_sum[len(nums)-1]-nums[0]))
        elif left_i == right_i == len(nums)-1:
            two = abs(prefix_sum[len(nums)-2] - nums[-1])
        else:
            if left_i == right_i:
                one = abs(prefix_sum[left_i] - (prefix_sum[len(nums)-1]-prefix_sum[left_i]))
                two = abs(prefix_sum[left_i-1] - (prefix_sum[len(nums)-1]  - prefix_sum[left_i-1]))
            elif left_i==right_i-1:
                one = abs(prefix_sum[left_i] - (prefix_sum[len(nums)-1]-prefix_sum[left_i]))
        ans = min(one, two)
        return -1 if ans == float("inf") else ans
