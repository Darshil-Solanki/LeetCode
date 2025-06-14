class Solution:
    def minMaxDifference(self, num: int) -> int:
        l = list(str(num))
        n = len(l)
        i = 0
        first_digit = l[0]
        
        while i<n-1 and l[i]=="9":
            i+=1
            first_digit = l[i]
        
        max_digit = int("".join([("9" if c==first_digit else c) for c in l]))

        i = 0
        first_digit = l[0]
        while i<n-1 and l[i]=="0":
            i+=1
            first_digit = l[i]
        
        min_digit = int("".join([("0" if c==first_digit else c) for c in l]))
        
        return max_digit-min_digit

        # more better readable from editorial
        # s = str(num)
        # t = s
        # pos = 0
        # while pos < len(s) and s[pos] == "9":
        #     pos += 1
        # if pos < len(s):
        #     s = s.replace(s[pos], "9")
        # t = t.replace(t[0], "0")
        # return int(s) - int(t)
