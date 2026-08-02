class Solution:
    def countRatioSubarrays(self, nums: list[int], a: int, b: int) -> int:
        n = len(nums)
        ab = a/b
        ans = 0
        
        for i in range(n):
            even, odd = 0, 0
            for j in range(i, n):
                if nums[j]%2:
                    odd += 1
                else:
                    even += 1
                if odd and even/odd <= ab:
                    ans += 1

        return ans
