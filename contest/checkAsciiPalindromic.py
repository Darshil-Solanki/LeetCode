class Solution:
    def isPalindromic(self, s: str) -> bool:
        ascii_bin = [bin(ord(c))[2:].rjust(8, "0") for c in s]
        new_str = "".join(ascii_bin)
        return new_str == new_str[::-1]
