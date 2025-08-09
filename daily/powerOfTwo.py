class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n<1: return False
        count = 0 
        while n>0:
            if n & 1:
                count += 1
                if count ==2: return False
            n >>= 1
        return count == 1
        
        # power = int(log(n, 2))
        # return (2**power)==n
