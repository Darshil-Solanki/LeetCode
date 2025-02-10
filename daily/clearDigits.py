class Solution:
    def clearDigits(self, s: str) -> str:
        temp = []
        for i, c in enumerate(s):
            if c.isdigit():
                temp.pop()
            else:
                temp.append(c)
        return "".join(temp)
