class Solution:
    def findValidPair(self, s: str) -> str:
        map = defaultdict(int)
        for c in s:
            map[c]+=1
        prev = s[0]
        for i in range(1, len(s)):
            curr = s[i]
            if prev!=curr and map[prev]==int(prev) and map[curr]==int(curr):
                return prev+curr
            prev = curr
        return ""
