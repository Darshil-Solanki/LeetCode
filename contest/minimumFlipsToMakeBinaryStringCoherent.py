class Solution:
    def minFlips(self, s: str) -> int:
        zero_count, one_count = s.count("0"), s.count("1")
        total = 0
        if zero_count==0:
            return 0
        if one_count == 2 and s == "1"+'0'*zero_count+"1":
            return 0
        if one_count>1:
            if s[0]=="1" and s[-1] =="1":
                return min(one_count - 2, zero_count)
            return min(one_count - 1, zero_count)
        return 0
