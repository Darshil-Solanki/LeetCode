class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        symbols = [(i, x)  for i, x in enumerate(dominoes) if x != '.']
        symbols = [(-1, 'L')] + symbols + [(len(dominoes), 'R')]

        ans = list(dominoes)
        for (left, x), (right, y) in zip(symbols, symbols[1:]):
            if x==y:
                for i in range(left+1, right):
                    ans[i] = x
            elif x>y: #R...L
                for i in range(left+1, right):
                    if i-left < right-i:
                        ans[i] = "R"
                    elif i-left == right-i:
                        ans[i] = "."
                    else:
                        ans[i] = "L"
        
        return "".join(ans)

        # n = len(dominoes)
        # force = [0]*n

        # # force from left to right
        # f = 0
        # for i, x in enumerate(dominoes):
        #     if x == "R": f = n
        #     elif x == "L": f = 0
        #     else: f = max(f-1, 0)
        #     force[i] += f
        
        # # force from right to left
        # f = 0
        # for i in range(n-1, -1, -1):
        #     if dominoes[i] == "L": f = n
        #     elif dominoes[i] == "R": f = 0
        #     else: f = max(f-1, 0)
        #     force[i] -= f
        
        # return "".join(('.' if f==0 else ('R' if f>0 else 'L')) for f in force)
