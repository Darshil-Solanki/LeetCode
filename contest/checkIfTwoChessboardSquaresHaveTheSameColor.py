class Solution:
    def checkTwoChessboards(self, coordinate1: str, coordinate2: str) -> bool:
        c1=c2=None
        if ord(coordinate1[0])%2==0:
            c1= 'black' if ord(coordinate1[1])%2==0 else 'white'
        else:
            c1 = 'white' if ord(coordinate1[1])%2==0 else 'black'
        if ord(coordinate2[0])%2==0:
            c2 = 'black' if ord(coordinate2[1])%2==0 else 'white'
        else:
            c2 = 'white' if ord(coordinate2[1])%2==0 else 'black'
        return c1==c2
