class Solution:
    def mySqrt(self, x: int) -> int:
        if not x or x==1:
            return x
        L, R = 1, x
        while L<=R:
            M = (L+R)//2
            mSquare = M*M
            if mSquare==x:
                return M 
            elif mSquare<x:
                L=M+1
            else:
                R=M-1
        return R
