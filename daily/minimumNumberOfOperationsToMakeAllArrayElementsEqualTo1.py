class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        no_1 = nums.count(1)
        g = reduce(gcd, nums)

        if no_1>0:
            return n - no_1
        if g>1:
            return -1

        min_len = n
        for i in range(n):
            g = 0
            for j in range(i, n):
                g = gcd(g, nums[j])
                if g == 1:
                    min_len = min(min_len, j-i+1)
                    break
        
        return min_len + n - 2
