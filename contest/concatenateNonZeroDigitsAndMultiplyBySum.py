class Solution:
    def sumAndMultiply(self, n: int) -> int:
        s = 0
        compress = i = 0

        while n>0:
            s += n%10
            if n%10:
                compress += (10**i)*(n%10)
                i+=1
            n //= 10
        
        return compress*s
