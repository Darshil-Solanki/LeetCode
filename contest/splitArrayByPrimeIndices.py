seive = [True]*1_00_001
seive[0] = seive[1] = False
for num in range(2, int(sqrt(1_00_001))+1):
    if seive[num]:
        for comp in range(num*num, 1_00_001, num):
            seive[comp] = False

class Solution:
    def splitArray(self, nums: List[int]) -> int:
        prime_sum, non_prime_sum = 0, 0
        for i, num in enumerate(nums):
            if seive[i]:
                prime_sum += num
            else:
                non_prime_sum += num

        return abs(prime_sum-non_prime_sum)
                
