class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for c in s:
            if c =="]":
                t = stack.pop()
                temp = ""
                while t!="[":
                    temp = t+temp
                    t = stack.pop()
                tempn=""
                n = stack.pop()
                while n.isdigit():
                    tempn = n+tempn
                    if stack:
                        n = stack.pop()
                    else:
                        break
                if stack:
                    stack.append(n)        
                stack.extend(list(temp*int(tempn)))
            else:
                stack.append(c)
        return "".join(stack)


# clean version
# class Solution:
#     def decodeString(self, s: str) -> str:
#         result = []
#         nums = set('1234567890')
#         for c in s:
#             if c != ']':
#                 result.append(c)
#             else:
#                 tmp = ""
#                 n = ""
#                 while result and result[-1] != '[':
#                     tmp = result.pop(-1) + tmp
#                 result.pop(-1)
#                 while result and result[-1] in nums:
#                     n = result.pop(-1) + n
#                 result.extend(int(n) * list(tmp))
#         return "".join(result)
