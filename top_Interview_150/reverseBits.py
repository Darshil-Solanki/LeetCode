class Solution:
    def reverseBits(self, n: int) -> int:
        nBin = bin(n)[2:]
        nBin = "0"*(32-len(nBin))+nBin
        return int(nBin[::-1],2)

# Better Solution In terms of maths     
# class Solution:
#     def reverseBits(self, n: int) -> int:
#         if n == 0:
#             return 0
#         output = 0
#         cnt = 31
#         while n != 0:
#             num = n % 2
#             output = output + num * pow(2, cnt)
#             n = int (n / 2)
#             cnt = cnt - 1

#         return output
