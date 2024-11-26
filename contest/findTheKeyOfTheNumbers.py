class Solution:
    def generateKey(self, num1: int, num2: int, num3: int) -> int:
        num1 = f'{num1:04}'
        num2 = f'{num2:04}'
        num3 = f'{num3:04}'
        result = ''
        for i in range(4):
            result += str(min(int(num1[i]),int(num2[i]),int(num3[i])))
        return int(result)
        
        # Better mathmatical solution
        # res = 0
        # for i in range(4):
        #     res += 10 ** i * min(num1 // (10 ** i) % 10, num2 // (10 ** i) % 10, num3 // (10 ** i) % 10)
        # return res
