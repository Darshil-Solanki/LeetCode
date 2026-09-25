class Solution:
    def braceExpansionII(self, expression: str) -> list[str]:
        operator, stack = [], []

        def popup():
            l, r = len(stack)-2, len(stack)-1
            if operator[-1]=="+":
                stack[l] |= stack[r]
            else:
                temp = set()
                for left in stack[l]:
                    for right in stack[r]:
                        temp.add(left+right)
                stack[l] = temp
            operator.pop()
            stack.pop()


        for i, c in enumerate(expression):
            match c:
                case ",":
                    while operator and operator[-1] == "*":
                        popup()
                    operator.append("+")
                case "{":
                    if i>0 and (expression[i-1] == "}" or expression[i-1].isalpha()):
                        operator.append("*")
                    operator.append("{")
                case "}":
                    while operator and operator[-1] != "{":
                        popup()
                    operator.pop()
                case _:
                    if i>0 and (expression[i-1]=="}" or expression[i-1].isalpha()):
                        operator.append("*")
                    stack.append({c})
        
        while operator:
            popup()
        
        return sorted(stack[-1])
