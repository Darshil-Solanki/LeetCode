class Solution:
    def hammingWeight(self, n: int) -> int:
        return bin(n)[2:].count('1')
    # Better Binary Calculation method
    # def hammingWeight(self, n: int) -> int:
    #     count = 0 
    #     for i in range(32):
    #         if (1 << i) & n:
    #             count += 1
        
    #     return count
