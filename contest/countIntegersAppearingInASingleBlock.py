class Solution:
    def countSpecialIntegers(self, nums: list[int]) -> int:
        n = len(nums)
        seen = defaultdict(int)
        i = 1
        ans = 1
        seen[nums[0]] = 1
        while i<n:
            if nums[i] == nums[i-1]:
                i += 1
                continue
            if seen[nums[i]] == 1:
                ans -= 1
                seen[nums[i]] = 2
            elif not seen[nums[i]]:
                ans += 1
                seen[nums[i]] = 1
            i += 1

        return ans
