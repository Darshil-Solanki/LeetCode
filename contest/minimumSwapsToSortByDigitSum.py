@cache
def get_digit_sum(num):
    digit_sum = 0
    
    while num>0:
        digit_sum += num%10
        num //= 10
        
    return digit_sum 
    
class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        new_arr = [0]*len(nums)

        for i, num in enumerate(nums):
            new_arr[i] = (get_digit_sum(num), num, i)

        new_arr.sort()
        ans = 0
        swaped = [False] * len(nums)

        for i in range(len(nums)):
            if swaped[i] or new_arr[i][2] == i:
                continue
            w = 0
            j = i
            while not swaped[j]:
                swaped[j] = True
                j = new_arr[j][2]
                w += 1
            ans += w - 1
        
        return ans
