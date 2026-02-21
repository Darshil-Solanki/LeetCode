class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        prime_set = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31}
        ans = 0
        for num in range(left, right+1):
            if bin(num).count("1") in prime_set:
                ans += 1
        
        return ans
