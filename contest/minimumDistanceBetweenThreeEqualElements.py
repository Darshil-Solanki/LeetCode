class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        n = len(nums)
        cnt = Counter(nums)
        ans = float("inf")
        
        for i, num in enumerate(nums):
            if cnt[num]>2:
                left = right = -1
                for l in range(i):
                    if nums[l] == num:
                        left = l

                for r in range(i+1, n):
                    if nums[r] == num:
                        right = r
                        break

                if left!=-1 and right!=-1:
                    ans = min(ans, 2*(right-left))

        return -1 if ans==float("inf") else ans
