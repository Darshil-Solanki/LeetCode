class Solution:
    def smallestUniqueSubarray(self, nums: List[int]) -> int:
        MOD = 1_000_000_007
        BASE = 911382323

        n = len(nums)
        h = [0] * (n + 1)
        p = [0] * (n + 1)
        p[0] = 1

        for i in range(n):
            h[i + 1] = (h[i] * BASE + nums[i]) % MOD
            p[i + 1] = p[i] * BASE % MOD
        

        def check(length):
            cnt = Counter()
            for l in range(n-length+1):
                r = l + length
                key = (h[r] - h[l] * p[length] % MOD + MOD) % MOD
                cnt[key] = cnt[key] + 1
            
            return 1 in cnt.values()
        
        left, right = 1, n
        while left < right:
            mid = (left+right) // 2
            if check(mid):
                right = mid
            else:
                left = mid + 1
        
        return left
