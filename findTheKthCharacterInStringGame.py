class Solution:
    def kthCharacter(self, k: int) -> str:
        alice = 'a'
        prev = ''
        while True:
            print(alice)
            if len(alice)>=k:
                return alice[k-1]
            if not prev:
                prev = 'b'
            else:
                prev = self.generatePrev(prev)
            alice += prev
    
    def generatePrev(self,s):
        res = ''
        for c  in s:
            res+=chr(ord(c)+1 if ord(c)!=122 else 97)
        return s+res
