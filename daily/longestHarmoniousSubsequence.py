class Solution:
    def findLHS(self, nums: List[int]) -> int:
        cnt = Counter(nums)
        ans = 0

        for num, count in cnt.items():
            if num+1 in cnt:
                ans = max(ans, count+cnt[num+1])
            
        return ans
