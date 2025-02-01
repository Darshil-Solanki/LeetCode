class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        n = nums[0]
        flag = True if n%2 else False
        for i in range(1, len(nums)):
            if flag:
                if nums[i]%2==0:
                    flag=False
                else:
                    return False
            else:
                if nums[i]%2!=0:
                    flag=True
                else:
                    return False
        return True
        # Short method
        # if len(nums) == 1:
        #     return True
        # for i in range(1,len(nums)):
        #     if (nums[i-1] % 2) == (nums[i] % 2):
        #         return False
        # return True
