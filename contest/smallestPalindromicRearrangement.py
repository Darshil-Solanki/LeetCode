class Solution:
    def smallestPalindrome(self, s: str) -> str:
        c = Counter(s)
        oddChar = ""
        ans = []
        for ch in "abcdefghijklmnopqrstuvwxyz":
            if ch in c:
                while c[ch]>1:
                    count = c[ch]
                    ans.append(ch)
                    c[ch]-=2
                if c[ch]==1: oddChar = ch
        return "".join(["".join(ans), "".join(ans[::-1])]) if len(s)%2==0 else "".join(["".join(ans), oddChar, "".join(ans[::-1])])
