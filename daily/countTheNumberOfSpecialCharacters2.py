class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        last_i = defaultdict(int)
        first_i = defaultdict(int)
        for i, c in enumerate(word):
            if 96<ord(c)<123:
                last_i[c] = i
            if 64<ord(c)<91 and c not in first_i:
                first_i[c] = i
        
        ans = 0
        for c, ci in last_i.items():
            if c.upper() in first_i and ci<first_i[c.upper()]:
                ans += 1
        
        return ans
