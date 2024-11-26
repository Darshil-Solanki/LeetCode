class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        def digitProduct(i):
            temp = 1
            while i>0:
                temp*=(i%10)
                i//=10
            return temp

        for i in range(n, n+1+t):
            if not digitProduct(i)%t:
                return i
