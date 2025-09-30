class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        n = len(nums)
        temp = nums[:]
        new = []
        for _ in range(len(temp)-1):
            for i in range(len(temp)-1):
                new.append((temp[i]+temp[i+1])%10)
            temp, new = new, []
        
        return temp[0]

        # using pascals triangle
        # n = len(nums)
        # ans, coeff = nums[0], 1

        # for i in range(1, n):
        #     coeff = coeff*(n-i)//i
        #     ans = (ans+coeff*nums[i])%10
        
        # return ans

    # using pascal triangle coefficient only half time as they are same for opposite side calculating both at same time
    # def triangularSum(self, nums: List[int]) -> int:
    #     n1 = len(nums) - 1
    #     c = 1
    #     ans = 0
    #     for i in range(floor(len(nums)/2)):
    #         ans = (ans + c*(nums[i]+nums[-1-i]))%10
    #         c *= n1 - i
    #         c //= i + 1
    #     if len(nums)%2: ans = (ans + c*nums[len(nums)//2])%10
    #     return ans
