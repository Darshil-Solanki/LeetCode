class Solution:
    def calculateScore(self, s: str) -> int:
        hashMap = defaultdict(list)
        score = 0
        seen = set()
        for i, c in enumerate(s):
            hashMap[c].append(i)
            mirror = chr(122+(97-ord(c)))
            if hashMap[mirror]:
                j = hashMap[mirror].pop()
                if j not in seen:
                    seen.add(i)
                    seen.add(j)
                    score+=(i-j)
        return score
