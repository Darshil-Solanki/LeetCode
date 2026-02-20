class Solution:
    def makeLargestSpecial(self, s: str) -> str:
        # copied from solutions
        ans = []
        cnt, j = 0, 0
        for i in range(len(s)):
            cnt += 1 if s[i] == "1" else -1
            if not cnt:
                ans.append('1'+self.makeLargestSpecial(s[j + 1 : i]) + '0')
                j = i+1
        ans.sort(reverse=True)
        return ''.join(ans)
