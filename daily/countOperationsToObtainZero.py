class Solution:
    def countOperations(self, num1: int, num2: int) -> int:
        if num1 == 0 or num2 == 0:
            return 0
            
        ops=0
        n1, n2 = max(num1, num2), min(num1, num2)
        while not (n1==0 or n2==0):
            n1, n2 = n1-n2, n2
            n1, n2 = max(n1, n2), min(n1, n2)
            ops+=1

        return ops

        # Editorial code # usage euclidean algo
        # res = 0  # total number of subtraction operations
        # while num1 and num2:
        #     # each step of the Euclidean algorithm
        #     res += num1 // num2
        #     num1 %= num2
        #     num1, num2 = num2, num1
        # return res
