is_prime = [True] * 1_000_001
is_prime[0] = is_prime[1] = False

for i in range(2, int(sqrt(1_000_001))+1):
    if is_prime[i]:
        for comp in range(i*i, 1_000_001, i):
            is_prime[comp] = False


class Solution:
    def maxPrimes(self, n: int, s: int) -> list[int]:
        ans = []
        tot = 0
        for i in range(2, n+1):
            if is_prime[i]:
                tot += i
                if tot>s:
                    break
                ans.append(i)

        return ans               
