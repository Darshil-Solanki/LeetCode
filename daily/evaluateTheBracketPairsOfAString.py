class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        data = defaultdict(lambda: "?")
        for k, v in knowledge:
            data[k] = v

        ans, temp = [], []
        flag = False
        for i, c in enumerate(s):
            if flag:
                if c == ")":
                    flag = False
                    key = "".join(temp)
                    temp = []
                    ans.append(data[key])
                else:
                    temp.append(c)
            else:
                if c == "(":
                    flag = True
                else:
                    ans.append(c)

        return "".join(ans)
