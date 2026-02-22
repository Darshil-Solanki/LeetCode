class Solution:
    def binaryGap(self, n: int) -> int:
        ans = 0
        temp = -1
        while n>0:
            if n&1:
                ans = max(ans, temp)
                temp = 1
                n>>=1
                continue
            n>>=1
            if temp != -1:
                temp += 1
        return ans
