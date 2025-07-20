class Solution:
    def checkDivisibility(self, n: int) -> bool:
        digit_sum = 0
        digit_product = 1
        num = n
        
        while n>0:
            digit_sum += n%10
            digit_product *= n%10
            n//=10
        
        return num % (digit_sum+digit_product) == 0
