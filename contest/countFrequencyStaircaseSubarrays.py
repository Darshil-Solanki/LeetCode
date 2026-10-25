class Solution:
    def countStaircase(self, nums: list[int]) -> int:
        n = len(nums)
        ans = 0
     
        for i in range(n):
            cnt, rank = {}, {}
            mismatches = 0
            
            for j in range(i, n):
                num = nums[j]

                if num not in cnt:
                    r = len(cnt) + 1
                    rank[num] = r
                    cnt[num] = 1
                    mismatches += (1 != r)
                else:
                    r = rank[num]
                    mismatches -= (cnt[num] != r)
                    cnt[num] += 1
                    mismatches += (cnt[num] != r)

                if mismatches == 0:
                    ans += 1
        return ans
