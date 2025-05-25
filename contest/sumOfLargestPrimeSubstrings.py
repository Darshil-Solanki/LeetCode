max_limit = 1_000_000
sieve = [0]*(max_limit+1)
sieve[0] = sieve[1] = 1
for i in range(2, isqrt(max_limit) + 1):
    if not sieve[i]:
        for j in range(i * i, max_limit + 1, i):
            sieve[j] = 1
@cache
def is_prime(n: int) -> bool:
    if n < max_limit:
        return not sieve[n]
    if n % 2 == 0 or n % 3 == 0:
        return False
    for i in range(5, isqrt(n) + 1,):
        if n % i == 0 :
            return False
    return True
    
class Solution:
    def sumOfLargestPrimes(self, s: str) -> int:
        heap = set()
        n = len(s)
        for i in range(n):
            curr = int(s[i])
            if is_prime(curr):
                heap.add(-curr)
            for j in range(i+1, n):
                curr = curr*10 + int(s[j])
                if is_prime(curr):
                    heap.add(-curr)


        heap = list(heap)
        heapify(heap)
        ans = 0
        for _ in range(3):
            if heap:
                ans += -heappop(heap)
        return ans
