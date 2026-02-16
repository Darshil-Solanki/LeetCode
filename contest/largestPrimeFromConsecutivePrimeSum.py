is_prime = [1]*5_00_001
prime_num = []
for i in range(2, 5_00_001):
    if is_prime[i]:
        prime_num.append(i)
    for comp in range(i+i, 5_00_001, i):
        is_prime[comp] = 0
        
class Solution:
    def largestPrime(self, n: int) -> int:
        tot = 0
        ans = 0
        for i, p in enumerate(prime_num):
            if tot+p>n:
               break
            tot += p
            if is_prime[tot]:
                ans = tot

        return ans
