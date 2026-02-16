class Solution:
    def reverseByType(self, s: str) -> str:
        temp = list(s)
        alphabet, sym = [], []
        for i, c in enumerate(temp):
            if c.isalpha():
                alphabet.append((c, i))
            else:
                sym.append((c, i))
        n, m = len(alphabet), len(sym)
        for i in range(n//2):
            c, idx = alphabet[i]
            c_end, idx_end = alphabet[n-i-1]
            temp[idx], temp[idx_end] = c_end, c

        for i in range(m//2):
            c, idx = sym[i]
            c_end, idx_end = sym[m-i-1]
            temp[idx], temp[idx_end] = c_end, c

        return "".join(temp)
