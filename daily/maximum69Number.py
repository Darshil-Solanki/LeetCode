class Solution:
    def maximum69Number (self, num: int) -> int:
        n = str(num)
        i = n.find("6")
        return num if i==-1 else int(n[:i]+"9"+n[i+1:])
