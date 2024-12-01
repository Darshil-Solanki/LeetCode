class Solution:
    def smallestNumber(self, n: int) -> int:
        return int("1"*len(bin(n)[2:]), 2)
        # return (1<<floor(log(n, 2)+1)) - 1
        # return int("1"*n.bit_length(),2)
