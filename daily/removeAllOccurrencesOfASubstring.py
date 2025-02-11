class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        stack = []
        n = len(part)
        for c in s:
            stack.append(c)
            if c==part[-1]:
                if "".join(stack[-n:])==part:
                    for _ in range(n):
                        stack.pop()
        return "".join(stack)

        # this one is faster may be because it doesn't have to do slicing plus time comeplexity is n*k where k is number of occurences instead of n*m where m is size of part
        # while part in s:
        #     s = s.replace(part,"",1)
        # return s
