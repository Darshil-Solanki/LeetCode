class Solution:
    def maxSubarraySum(self, nums: List[int], k: int) -> int:
        # copied from submission
        def solve(transform):
            NEG_INF = float("-inf")
            dp0 = dp1 = dp2 = ans = NEG_INF
            for num in nums:
                t_num = transform(num)

                old0, old1, old2 = dp0, dp1, dp2

                dp0 = max(num, old0+num)

                dp1 = max(t_num, (old0+t_num), (old1+t_num))

                dp2 = max(old1+num, old2+num)

                ans = max(ans, dp0, dp1, dp2)
            
            return ans
        
        def divide(x):
            if x>-1:
                return x//k
            return -((-x)//k)
        
        return max(solve(lambda x: x*k), solve(divide))
