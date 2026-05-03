class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if s==goal:
            return True
        n = len(s)
        ls = list(s)
        for i in range(n):
            left, right = ls[:i], ls[i:]
            if "".join(right+left)==goal:
                return True
        return False
