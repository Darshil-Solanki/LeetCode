class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        cases = [(1, 0), (0, 1), (0, 0), (1, 1)]
        ans = 0

        for case in cases:
            cnt = 0
            for num in nums:
                if num%2 == case[cnt%2]:
                    cnt += 1
            ans = max(ans, cnt)
        
        return ans
