class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        def get_sum(num):
            digit_sum = 0
            
            while num>0:
                digit_sum += num%10
                num //=10

            return digit_sum

        for i, num in enumerate(nums):
            if get_sum(num)==i:
                return i

        return -1
