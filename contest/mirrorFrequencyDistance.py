class Solution:
    def mirrorFrequency(self, s: str) -> int:
        cnt = Counter(s)
        ans = 0
        seen = set()
        characters = string.ascii_lowercase
        
        for c, val in cnt.items():
            mirror = str(9-int(c)) if c.isdigit() else chr(219-ord(c))
            if mirror not in seen:
                seen.add(c)
                seen.add(mirror)
                ans += abs(cnt[c]-cnt[mirror])

        return ans
