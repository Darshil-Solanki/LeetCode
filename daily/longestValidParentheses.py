class Solution:
    def longestValidParentheses(self, s: str) -> int:
        ans = 0
        stack = [-1]

        for i, c in enumerate(s):
            if c == "(":
                stack.append(i)
            else:
                stack.pop()

            if not stack:
                stack.append(i)

            ans = max(ans, i-stack[-1])

        return ans
www
