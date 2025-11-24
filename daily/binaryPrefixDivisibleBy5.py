class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        n = 0
        ans = [False]*len(nums)

        for i, x in enumerate(nums):
            n = ((n<<1)+x) % 5
            if n==0:
                ans[i] = True
        
        return ans
