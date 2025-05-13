class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        MOD = 1_000_000_007
        cnt = [0]*26 # Counter for character 0=a ....25=z
        
        for c in s:
            cnt[ord(c)-ord("a")] += 1

        for _ in range(t):
            nxt = [0]*26
            nxt[0] = cnt[25]
            nxt[1] = ( cnt[25]+cnt[0] ) % MOD
            for i in range(2, 26):
                nxt[i] = cnt[i-1]
            cnt = nxt
        
        return sum(cnt) % MOD
