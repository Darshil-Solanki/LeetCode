class Solution:
    def getLongestArithmetic(self, nums: list[int]) -> int:
        # from solutions
        max_len = 2
        diff = nums[1] - nums[0]
        n = len(nums)
        
        l = 0
        r = 2
        while r < n:
            cur_diff = nums[r] - nums[r - 1]
            if cur_diff == diff:
                max_len = max(max_len, r - l + 1)
                r += 1
                continue
            
            pre_r = r
            tmp_r = r
            cur = nums[r - 1] + diff
            while tmp_r + 1 < n and nums[tmp_r + 1] - cur == diff:
                cur = nums[tmp_r + 1]
                tmp_r += 1
            
            max_len = max(max_len, tmp_r - l + 1)
            l = pre_r - 1
            diff = cur_diff
            r += 1
        
        return max_len

    def longestArithmetic(self, nums: list[int]) -> int:
        max_len = self.getLongestArithmetic(nums)
        nums.reverse()
        return max(max_len, self.getLongestArithmetic(nums))
