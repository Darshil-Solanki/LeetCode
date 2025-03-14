class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        def check(k_candy):
            curr_k = 0
            for c in candies:
                curr_k+=(c//k_candy)
            
            if curr_k>=k: return True
            return False


        if sum(candies)<k: return 0
        left, right = 1, max(candies)
        
        while left<=right:
            mid = (left+right)//2
            if check(mid):
                left = mid+1
            else:
                right = mid-1
        
        return right
