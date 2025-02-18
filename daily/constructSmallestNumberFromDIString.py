class Solution:
    def smallestNumber(self, pattern: str) -> str:
        n = len(pattern)
        seen = set()

        def backtrack(i, curr):
            if i==n+1:
                return curr 

            for num in range(1, n+2):
                if num in seen:
                    continue
                if not i or (pattern[i-1]=="I" and curr[-1]<str(num)) or (pattern[i-1]=="D" and curr[-1]>str(num)):
                    seen.add(num)
                    res = backtrack(i+1, curr+str(num))
                    seen.remove(num)
                    if res:
                        return res

            return ""
        return backtrack(0, "")

        # stack greedy method
        # result = []
        # stack = []

        # for i in range(len(pattern) + 1):
        #     stack.append(str(i + 1))
        #     if i == len(pattern) or pattern[i] == 'I':
        #         while stack:
        #             result.append(stack.pop())

        # return "".join(result)
