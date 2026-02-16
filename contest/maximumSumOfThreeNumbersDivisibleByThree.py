class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        mod_max = defaultdict(list)
        for num in nums:
            mod = (num+3)%3
            mod_max[mod].append(num)

        for i in range(3):
            mod_max[i].sort()

        zero_one_two_mod = (mod_max[0][-1]+mod_max[1][-1]+mod_max[2][-1]) if (mod_max[0] and mod_max[1] and mod_max[2]) else 0 
        all_zero_mod = sum(mod_max[0][-3:]) if len(mod_max[0])>2 else 0
        all_one_mod = sum(mod_max[1][-3:]) if len(mod_max[1])>2 else 0
        all_two_mod = sum(mod_max[2][-3:]) if len(mod_max[2])>2 else 0

        return max(zero_one_two_mod, all_zero_mod, all_one_mod, all_two_mod)
