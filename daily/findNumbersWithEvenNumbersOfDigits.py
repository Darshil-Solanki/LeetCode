class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        ans = 0

        # def get_digit_count(num):
        #     if not num: return 1
        #     count = 0

        #     while num>0:
        #         count += 1
        #         num //= 10
            
        #     return count

        for num in nums:
            if len(str(num))%2==0:
                ans += 1
        return ans
