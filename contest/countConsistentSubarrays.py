class Solution:
    def countConsistent(self, nums: list[int]) -> int:
        n = len(nums)
        ans = 0
        
        for i in range(n):
            mn = bit_and = nums[i]
            ans += 1
            for j in range(i+1, n):
                mn = min(nums[j], mn)
                bit_and &= nums[j]
                if bit_and == mn:
                    ans += 1

        return ans
