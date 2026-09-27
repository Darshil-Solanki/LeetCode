class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        
        for c in s:
            match c:
                case ")":
                    temp = []
                    while stack and stack[-1] != "(":
                        temp.append(stack.pop())
                    stack.pop()
                    stack.extend(temp)
                case _:
                    stack.append(c)

        return "".join(stack)
