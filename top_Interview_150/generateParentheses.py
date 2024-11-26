class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def backtrack(curr, open, i):
            if i == n:
                res.append(curr + (")" * open))
                return
            if i < n:
                curr += "("
                backtrack(curr, open + 1, i + 1)
                curr = curr[:-1]
                if open > 0:
                    curr += ")"
                    backtrack(curr, open - 1, i)
                    curr = curr[:-1]

        backtrack("(", 1, 1)
        return res

    # Little bit improve version
    # def generateParenthesis(self, n: int) -> List[str]:
    #     def form(s, o, c):
    #         if o == n:
    #             return [s + ")" * (n - c)]
    #         else:
    #             if o == c:
    #                 return form(s + "(", o + 1, c)
    #             else:
    #                 if o > c:
    #                     return form(s + "(", o + 1, c) + form(s + ")", o, c + 1)

    #     return form("", 0, 0)
