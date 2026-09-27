class Solution:
    def maxSubarray(self, nums: List[int]) -> int:
        cnt = Counter()
        left, ans = 0, 0

        def check(x):
            return ( any(cnt[a] and cnt[x - a] > (2*a == x) for a in range(1, x)) 
            or any(cnt[b] > (b == x) and cnt[x + b] for b in range(1, 501)) )

        for right, num in enumerate(nums):
            cnt[num] += 1
            
            while check(num):
                cnt[nums[left]] -= 1
                left += 1

            ans = max(ans, right-left+1)

        return ans
