class Solution:
    def maximumProduct(self, nums: List[int], m: int) -> int:
        n = len(nums)
        if m == 1:
            min_num = min(nums)
            max_num = max(nums)
            return max(min_num*min_num, max_num*max_num)
        min_element = [float("inf")]*n
        max_element = [float("-inf")]*n
        for i in range(n-1, max(-1, m-2), -1):
            num = nums[i]
            next_min_element = min_element[i+1] if i<n-1 else float("inf")
            next_max_element = max_element[i+1] if i<n-1 else float("-inf")
            min_element[i] = min(num, next_min_element)
            max_element[i] = max(num, next_max_element)

        
        ans = float("-inf")
        for i, num in enumerate(nums):
            if n-(i+m)<0: break
            min_product = num * min_element[i+m-1]
            max_product = num * max_element[i+m-1]
            ans = max(ans, min_product, max_product)
        
        return ans
