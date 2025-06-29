class Solution:
    def minXor(self, nums: List[int], k: int) -> int:
        n = len(nums)
        
        @cache
        def dp(index, parts):
            if parts == 0:
                if  index == n:
                    return 0
                return float("inf")
                
            if  index == n:
                return float("inf")

            curr = 0
            ans = float("inf")

            for i in range(index, n-(parts-1)):
                curr ^= nums[i]
                nxt = dp(i+1, parts-1)
                maximum = max(curr, nxt) 
                ans = min(ans, maximum)
            
            return ans
        
        return dp(0, k)
