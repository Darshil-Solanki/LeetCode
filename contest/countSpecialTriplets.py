class Solution:
    def specialTriplets(self, nums: List[int]) -> int:
        MOD = 1_000_000_007
        left = defaultdict(int)
        right = Counter(nums)
        n = len(nums)
        ans = 0
        
        for i, num in enumerate(nums):
            double_num = num*2
            left_count = left[double_num]
            left[num] += 1
            right[num] -= 1
            right_count = right[double_num]
            if left_count and right_count:
                ans = (ans + left_count * right_count) % MOD

        return ans
