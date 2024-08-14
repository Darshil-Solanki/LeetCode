class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = [0]*n
        prefix[0] = nums[0]
        for i in range(1,n):
            prefix[i]=nums[i]*prefix[i-1]
        suffix = [0]*n
        suffix[-1] = nums[-1]
        for i in range(n-2,-1,-1):
            suffix[i]=suffix[i+1]*nums[i]
        result = []
        for i in range(n):
            if i==0:
                result.append(suffix[i+1])
            elif i==n-1:
                result.append(prefix[i-1])
            else:
                result.append(prefix[i-1]*suffix[i+1])
        return result
    
    # Better way doing this same code with memory efficeint
    # def productExceptSelf(self, nums: List[int]) -> List[int]:
    #     res = [1]*len(nums)
    #     prefix = 1
    #     for i in range(len(nums)):
    #         res[i] = prefix
    #         prefix *= nums[i]
    #     postfix = 1
    #     for i in range(len(nums) -1,-1,-1):
    #         res[i] *= postfix
    #         postfix *=nums[i]
    #     return res
