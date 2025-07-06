class Solution:
    def concatHex36(self, n: int) -> str:
        n2 = n*n
        n3 = n**3
        hexd, hext = [], []
        while n2>0:
            rem = n2 % 16
            if rem>9:
                hexd.append(chr(55+rem))
            else:
                hexd.append(str(rem))
            n2 //= 16
        while n3>0:
            rem = n3 % 36
            if rem>9:
                hext.append(chr(55+rem))
            else:
                hext.append(str(rem))
            n3 //= 36
        return "".join(hexd[::-1]+hext[::-1])
