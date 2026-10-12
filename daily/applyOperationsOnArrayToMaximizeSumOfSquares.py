class Solution:
    def maxSum(self, nums: List[int], k: int) -> int:
        MOD = 1_000_000_007
        cnt = [0] * 30

        for num in nums:
            for i in range(30):
                if num & (1<<i):
                    cnt[i] += 1
        
        ans = 0
        for _ in range(k):
            curr = 0
            for j in range(29, -1, -1):
                if cnt[j]:
                    curr |= 1<<j
                    cnt[j] -= 1
            ans = (ans + curr * curr) % MOD
        
        return ans
