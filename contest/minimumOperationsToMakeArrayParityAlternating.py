class Solution:
    def makeParityAlternating(self, nums: List[int]) -> List[int]:
        def solve(even):
            op = 0
            mx, mn = float("-inf"), float("inf")
            for num in nums:
                if (num%2 and even) or (num%2==0 and not even):
                    op += 1
                    mx, mn = max(mx, num-1), min(mn, num+1)
                else:
                    mx, mn = max(mx, num), min(mn, num)
                even = not even
            return [op, mx-mn]
        
        if len(nums)==1: return [0, 0]
        if len(set(nums)) == 1:
            return [len(nums)//2, 1]
        
        ans1 = solve(True)
        ans2 = solve(False)
        if ans1[0]==ans2[0]:
            return ans1 if ans1[1]<ans2[1] else ans2
        return ans1 if ans1[0]<ans2[0] else ans2
