class Solution:
    def checkGoodInteger(self, n: int) -> bool:
        digit_sum = 0
        square_sum = 0
        
        for c in str(n):
            d = int(c)
            digit_sum += d
            square_sum += d*d

        return square_sum - digit_sum >= 50
