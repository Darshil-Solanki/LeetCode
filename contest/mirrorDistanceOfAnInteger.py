class Solution:
    def mirrorDistance(self, n: int) -> int:
        reverse = 0
        original = n
        while n>0:
            reverse = reverse*10 + n%10
            n//=10

        return abs(original-reverse)
