class Solution:
    def maximumXor(self, s: str, t: str) -> str:
        n = len(t)
        t_zero_count = t.count("0")
        t_one_count = n-t_zero_count
        ans = []
        
        for i, c in enumerate(s):
            if c == "1":
                if t_zero_count:
                    ans.append("1")
                    t_zero_count -= 1
                else:
                    ans.append("0")
                    t_one_count -= 1
            else:
                if t_one_count:
                    ans.append("1")
                    t_one_count -= 1
                else:
                    ans.append("0")
                    t_zero_count -= 1

        return "".join(ans)
        
