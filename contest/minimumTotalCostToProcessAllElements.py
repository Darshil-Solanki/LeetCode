class Solution:
    def minimumCost(self, nums: list[int], k: int) -> int:
        MOD = 1_000_000_007
        ops = 0
        resources = k

        for num in nums:
            if resources<num:
                curr_ops = ceil((num - resources) / k)
                ops += curr_ops
                resources += curr_ops*k
            resources -= num

        return (ops*ops + ops) // 2 % MOD
