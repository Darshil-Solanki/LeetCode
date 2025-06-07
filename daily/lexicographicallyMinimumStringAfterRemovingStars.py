class Solution:
    def clearStars(self, s: str) -> str:
        indices = [ [] for _ in range(26)]
        l = list(s)
        for i, c in enumerate(l):
            if c != "*":
                indices[ord(c)-97].append(i)
            else:
                for j in range(26):
                    if indices[j]:
                        l[indices[j].pop()] = "*"
                        break
                
        return "".join( c for c in l if c != "*")
