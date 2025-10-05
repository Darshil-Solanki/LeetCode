class Solution:
    def removeSubstring(self, s: str, k: int) -> str:
        stack = []
        for c in s:
            if stack and stack[-1][0] == c:
                stack[-1][1] += 1
            else:
                stack.append([c, 1])
                
            while len(stack)>1:
                if stack[-2][0]=="(" and stack[-1][0]==")":
                    remove = min(stack[-2][1]//k, stack[-1][1]//k)
                    if not remove:
                        break
                    stack[-2][1] -= remove*k
                    stack[-1][1] -= remove*k
                    if not stack[-1][1]:
                        stack.pop()
                    if stack[-1][0] == "(" and not stack[-1][1]:
                        stack.pop()
                    
                    if len(stack)>1 and stack[-2][0] == stack[-1][0]:
                        stack[-2] = (stack[-2][0], stack[-2][1] + stack[-1][1])
                        stack.pop()
                else:
                    break

        return "".join(c*cnt for c, cnt in stack)

        # pythonic way faster for smaller length only but gets accepted for 10^5 length because only 4-5 testcase has recursive deletion 
        # ans = s
        # t = '(' * k + ')' * k
        # while True:
        #     n = ans.replace(t, '')
        #     if n == ans:
        #         break
        #     ans = n
        # return ans
