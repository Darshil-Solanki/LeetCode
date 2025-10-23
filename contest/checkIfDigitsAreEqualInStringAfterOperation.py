class Solution:
    def hasSameDigits(self, s: str) -> bool:
        while len(s)>2:
            value = ""
            for i in range(1, len(s)):
                value+=str((int(s[i-1])+int(s[i]))%10)
            s = value
        return s[0]==s[1]

        # ord and storing value is faster than calculating using int 
        # n = len(s)
        # if n<=3:
        #     return s[0] == s[-1]
        # v1 = v2 = 0
        # c = 1
        # s_int = [ord(ch)-48 for ch in s]

        # n1 = n-1
        # for i in range(n):
        #     v1 += s_int[i] * c
        #     v2 += s_int[n1-i] * c
        #     c = c * (n1 - i - 2)//(i+1)

        # return (v1 - v2) % 10 == 0
