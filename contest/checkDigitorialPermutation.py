class Solution:
    def isDigitorialPermutation(self, n: int) -> bool:
        fact = {0:1, 1:1, 2:2, 3:6, 4:24, 5:120, 6:720, 7:5040, 8:40320, 9:362880}
        fact_sum = 0
        temp = n
        
        while temp>0:
            d = temp%10
            fact_sum += fact[d]
            temp //= 10
            
        return sorted(str(n)) == sorted(str(fact_sum))
