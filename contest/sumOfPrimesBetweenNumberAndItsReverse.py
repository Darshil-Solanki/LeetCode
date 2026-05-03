@cache
def reverse(n):
    temp = 0
    while n>0:
        temp = temp*10 + n%10
        n//=10
    return temp

is_prime = [True]*1001
is_prime[0] = is_prime[1] = False
for i in range(2, int(sqrt(1001))+1):
    if is_prime[i]:
        for j in range(i*i, 1001, i):
            is_prime[j]=False
        

class Solution:
    def sumOfPrimesInRange(self, n: int) -> int:
        rev = reverse(n)
        left, right = min(n, rev), max(n, rev)
        return sum(num for num in range(left, right+1) if is_prime[num])
