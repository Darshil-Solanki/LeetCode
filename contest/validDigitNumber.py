class Solution:
    def validDigit(self, n: int, x: int) -> bool:
        str_n = str(n)
        return str(x) in str_n[1:] and str_n[0]!=str(x)
