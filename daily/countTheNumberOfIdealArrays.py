MOD = 1_000_000_007
MAX_N = 10_000+1
MAX_P = 15 # maximum 15 prime factors of a number

# sieve algo for prime numbers
sieve = [0]*MAX_N
for i in range(2, MAX_N):
    if sieve[i]==0:
        for j in range(i, MAX_N, i):
            sieve[j]=i

# contain count of prime factors for each number
ps = [[] for _ in range(MAX_N)]

for i in range(2, MAX_N):
    x = i
    while x>1:
        p = sieve[x]
        cnt = 0
        while x%p==0:
            x //= p
            cnt+=1
        ps[i].append(cnt)

# dp to find combinations (binomial coefficient matches pascal's triangle)
c = [[0]*(MAX_P+1) for _ in range(MAX_N+MAX_P)]

c[0][0] = 1
for i in range(1, MAX_N+MAX_P):
    c[i][0] = 1
    for j in range(1, min(i, MAX_P)+1):
        c[i][j] = ( c[i-1][j] + c[i-1][j-1] )%MOD


class Solution:
    def idealArrays(self, n: int, maxValue: int) -> int:
        ans = 0

        for x in range(1, maxValue+1):
            mul = 1
            for p in ps[x]:
                mul = mul * c[n+p-1][p] % MOD # n-1 stars and p bars
            
            ans = (ans+mul) % MOD
        
        return ans
