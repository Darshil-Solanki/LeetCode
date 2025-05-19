class Solution:
    def triangleType(self, nums: List[int]) -> str:
        a, b, c = nums
        if a+b>c and a+c>b and c+b>a:
            side = set(nums)
            if len(side)==1: return "equilateral"
            if len(side)==2: return "isosceles"
            return "scalene"
        else:
            return "none"
