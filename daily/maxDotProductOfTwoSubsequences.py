class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        m, n = len(nums1), len(nums2)
        
        @cache
        def dp(i, j):
            if i == m or j == n:
                return float("-inf")
        
            take = nums1[i]*nums2[j]
            ans = max(take+dp(i+1, j+1), take, dp(i+1, j), dp(i, j+1))
            return ans
        
        return dp(0, 0)
