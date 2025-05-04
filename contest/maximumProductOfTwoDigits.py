class Solution:
    def maxProduct(self, n: int) -> int:
        l = list(map(int, list(str(n))))
        l.sort()
        two = l[-2:]
        return two[0]*two[1]
