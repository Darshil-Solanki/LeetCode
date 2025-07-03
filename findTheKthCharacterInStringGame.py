class Solution:
    def kthCharacter(self, k: int) -> str:
        alice = 'a'
        while True:
            if len(alice)>=k:
                return alice[k-1]
            alice = self.generatePrev(alice)
    
    def generatePrev(self,s):
        return "".join([s]+[(chr(ord(c)+1 if ord(c)!=122 else 97)) for c  in s])
    
    # Editorial ways 
    # def kthCharacter(self, k: int) -> str:
    #     ans = 0
    #     while k != 1:
    #         t = k.bit_length() - 1
    #         if (1 << t) == k:
    #             t -= 1
    #         k -= 1 << t
    #         ans += 1
    #     return chr(ord("a") + ans)
