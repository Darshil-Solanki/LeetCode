class Solution:
    def minOperations(self, s: str) -> int:
        if len(s)==1:
            return 0
        elif len(s) == 2:
            return -1 if s[0]>s[1] else 0
        sorted_str = "".join(sorted(s))
        if s==sorted_str:
            return 0
        elif s[0]==sorted_str[0] or s[-1]==sorted_str[-1]:
            return 1
        first = s.index(sorted_str[0])
        if first==len(s)-1:
            curr = "".join(sorted(s[1:]))
            if s[0]>curr[-1]:
                return 3
            return 2
        curr = "".join(sorted(s[:first+1]))+s[first+1:]
        if curr=="".join(sorted(curr)):
            return 1
        return 2

        # better solutions same idea
        # if len(s) == 2 and s[0] > s[1]:
        #     return -1
        # if all(s[i] <= s[i+1] for i in range(len(s)-1)):
        #     return 0
        # if s[0] == (a := min(s)) or s[-1] == (z := max(s)):
        #     return 1
        # if s[0] == z and s[-1] == a and s.count(a) == s.count(z) == 1:
        #     return 3
        # return 2
