class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        length = len(nums)
        result = []
        for i, n in enumerate(nums):
            if not n: 
                result.append(0)
            elif n>0:
                result.append(nums[(i+n)%length])
            else:
                result.append(nums[(length+i+n)%length])
        return result
