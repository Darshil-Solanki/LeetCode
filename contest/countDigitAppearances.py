class Solution:
    def countDigitOccurrences(self, nums: list[int], digit: int) -> int:
        digit_str = str(digit)
        ans = 0
        for num in nums:
            ans += str(num).count(digit_str)
        return ans
