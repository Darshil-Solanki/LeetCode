class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        prev = s[0]
        groups = []
        temp = 0
        for c in s:
            if c == prev:
                temp += 1
                prev = c
                continue
            prev = c
            groups.append(temp)
            temp = 1
        groups.append(temp)
        
        ans = 0
        for i in range(len(groups)-1):
            ans += min(groups[i], groups[i+1])
        
        return ans
