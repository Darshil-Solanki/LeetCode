class Solution:
    def partitionString(self, s: str) -> List[str]:
        seen = defaultdict(bool)
        curr = ""
        ans = []
        
        for i, c in enumerate(s):
            if seen[curr+c]:
                curr += c
            else:
                seen[curr+c] = True
                ans.append(curr+c)
                curr = ""

        return ans
