class Solution:
    def subsequenceSumAfterCapping(self, nums: List[int], k: int) -> List[bool]:
        nums.sort()
        n = len(nums)
        ans =[False]*n
        dp = 1
        mask = (1<<k+1)-1
        i = 0
        for x in range(1, n+1):
            if not ans[x-1]:
                while i<n and nums[i]<=x:
                    dp |= (dp<<nums[i]) & mask
                    i += 1
                v = max( k % x, k-(n-i)*x )
                for j in range(v, k+1, x):
                    if dp & (1<<j):
                        ans[x-1] = True
                        break
        return ans
