@cache
def invert(s):
    return "".join([("1" if c=="0" else "0")for c in s])
@cache
def reverse(s):
    return s[::-1]
curr = "0"
bin_str = ["", "0"]
for i in range(2, 21):
    curr += ("1" + reverse(invert(curr)))
    bin_str.append(curr[:])

class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        return bin_str[n][k-1]
