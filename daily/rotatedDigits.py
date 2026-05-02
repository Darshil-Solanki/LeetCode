ans = [0]*10_001

def valid(num):
    digits = {i:False for i in range(10)}
    while num>0:
        if num%10 in (3, 4, 7):
            return False
        digits[num%10] = True
        num //= 10
    if any(digits[d] for d in (2, 5, 6, 9)):
        return True
    return False

for i in range(1, 10_001):
    ans[i] = ans[i-1]+valid(i)

class Solution:
    def rotatedDigits(self, n: int) -> int:
        return ans[n]
