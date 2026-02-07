class Solution:
    def minimumDeletions(self, s: str) -> int:
        n = len(s)
        b_prefix, a_suffix = [], [0]*n
        
        temp = 0
        for c in s:
            b_prefix.append(temp)
            if c=="b":
                temp += 1
        temp = 0
        for i in range(n-1, -1, -1):
            a_suffix[i] = temp
            if s[i]=="a":
                temp += 1
        
        ans = float("inf")
        for b, a in zip(b_prefix, a_suffix):
            ans = min(ans, b+a)
        
        return ans
