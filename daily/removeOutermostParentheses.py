class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        stack = []
        open_b = 0

        for c in s:
            if c == ")":
                open_b -= 1
                if open_b:
                    stack.append(c)
            else:
                if open_b:
                    stack.append(c)
                open_b += 1
        
        return "".join(stack)
