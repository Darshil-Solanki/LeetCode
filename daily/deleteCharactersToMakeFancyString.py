class Solution:
    def makeFancyString(self, s: str) -> str:
        stack = []
        prev = ""
        count = 0

        for c in s:
            stack.append(c)
            if c==prev:
                count += 1
            else:
                count = 1
            if count == 3:
                stack.pop()
                count -=1
            prev = c

        return "".join(stack)
