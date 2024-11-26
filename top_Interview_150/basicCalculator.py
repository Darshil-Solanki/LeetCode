class Solution:
    def calculate(self, s: str) -> int:
        #learned from youtube
        currNum, result, sign, stack = 0, 0, 1, []
        for c in s:
            match c:
                case " ":
                    continue
                case "+" | "-":
                    result += (currNum*sign)
                    currNum = 0
                    sign = -1 if c=="-" else 1
                case "(":
                    stack.append(result)
                    stack.append(sign)
                    currNum, sign = 0, 1
                    result = 0
                case ")":
                    result+=(currNum*sign)
                    result*=stack.pop()
                    result+=stack.pop()
                    currNum = 0
                case _:
                    currNum = currNum*10+int(c)
        return result+(currNum*sign)
