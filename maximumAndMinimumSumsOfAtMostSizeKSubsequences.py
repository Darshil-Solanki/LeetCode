class Solution:
    def minMaxSums(self, nums: List[int], k: int) -> int:
        nums.sort()
        tot = 0
        times = 1

        for i, num in enumerate(nums):
            tot += times*(num + nums[-i-1])
            times = 2 * times - comb(i, k-1)

        return tot%1_000_000_007
