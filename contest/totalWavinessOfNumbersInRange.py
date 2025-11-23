class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        def get_waviness(num):
            if num<101:
                return 0
            digit = list(map(int, str(num)))
            ans = 0
            for i in range(1, len(digit)-1):
                if digit[i-1]<digit[i]>digit[i+1]:
                   ans += 1
                elif digit[i-1]>digit[i]<digit[i+1]:
                    ans += 1
            return ans
            
        return sum(get_waviness(n) for n in range(num1, num2+1))
