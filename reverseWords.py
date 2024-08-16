class Solution:
    def reverseWords(self, s: str) -> str:
        revStr = s.split()[::-1]
        res = ""
        for i in revStr:
            if i:
                res+=i+" "
        return res[:len(res)-1]

        # One Line Better Solution
        # return " ".join(reversed(s.split()))
