class Solution:
    def countSequences(self, nums: List[int], k: int) -> int:
        self.ans = 0
        n = len(nums)
        
        @cache
        def dp(i, numerator, denominator):
            if i == n:
                if numerator/denominator==k:
                    return 1
                return 0
            return sum([dp(i+1, numerator*nums[i], denominator),
                    dp(i+1, numerator, denominator),
                    dp(i+1, numerator, denominator*nums[i])])

        return dp(0, 1, 1)
