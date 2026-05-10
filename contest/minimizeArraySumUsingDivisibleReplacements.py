MAX=100_001
factors = [[] for _ in range(MAX)]
for i in range(2, MAX):
    for j in range(i, MAX, i):
        factors[j].append(i)

class Solution:
    def minArraySum(self, nums: list[int]) -> int:
        num_set = set(nums)
        if 1 in num_set:
            return len(nums)

        tot = 0
        for n in nums:
            for p in factors[n]:
                if p in num_set:
                    tot += p
                    break

        return tot        
