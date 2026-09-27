class Solution:
    def rearrangeArray(self, nums: list[int]) -> list[int]:
        cnt = Counter(nums)
        unique = list(sorted(cnt.keys()))
        unique_len = len(unique)
        ans = []
        i = 0
        
        while cnt:
            num = unique[i]
            if cnt[num]:
                ans.append(num)
                cnt[num] -= 1
                if cnt[num]==0:
                    del cnt[num]
            i = (i+1) % unique_len

        return ans
