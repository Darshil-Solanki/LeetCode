class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        prev = 0
        for c in bin(n)[2:]:
            if c == prev:
                return False
            prev = c
        return True
        
        # xor solution
        # x = n ^ (n>>1)
        # return (x&(x+1))==0
