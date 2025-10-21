class Solution:
    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:
        nums.sort()
        cnt = Counter(nums)
        ans = cnt.most_common(1)[0][1]

        for i in range(nums[0], nums[-1]+1):
            l = bisect_left(nums, i-k)
            r = bisect_right(nums, i+k) - 1
            if i in cnt:
                temp = min(r-l+1, cnt[i]+numOperations)
            else:
                temp = min(r-l+1, numOperations)
            ans = max(ans, temp)

        return ans
