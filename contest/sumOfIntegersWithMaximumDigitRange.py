class Solution:
    def maxDigitRange(self, nums: list[int]) -> int:
        digit_range = defaultdict(list)
        max_digit_r = -1
        
        for num in nums:
            s_num = str(num)
            digit_r = int(max(s_num))-int(min(s_num))
            max_digit_r = max(max_digit_r, digit_r)
            digit_range[digit_r].append(num)
        
        return sum(digit_range[max_digit_r])
