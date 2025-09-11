class Solution:
    def sortVowels(self, s: str) -> str:
        ans = list(s)
        v_chr, v_idx = [],  []
        
        for i, c in enumerate(s):
            if c.lower() in ["a","e","i", "o", "u"]:
                v_idx.append(i)
                v_chr.append(c)
        
        v_chr.sort()
        for i, v_c in zip(v_idx, v_chr):
            ans[i] = v_c
        
        return "".join(ans)
