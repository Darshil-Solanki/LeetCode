class Solution:
    def flowerGame(self, n: int, m: int) -> int:
        odd_even = ceil(n/2)*(m//2)
        even_odd = (n//2)*ceil(m/2)
        return odd_even + even_odd
