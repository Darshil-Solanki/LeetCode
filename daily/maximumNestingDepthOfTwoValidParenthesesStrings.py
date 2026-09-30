class Solution:
    def maxDepthAfterSplit(self, seq: str) -> list[int]:
        ans = []
        stack = 0

        for c in seq:
            if c == "(":
                stack += 1
                ans.append(stack % 2)
            else:
                ans.append(stack % 2)
                stack -= 1
        return ans
