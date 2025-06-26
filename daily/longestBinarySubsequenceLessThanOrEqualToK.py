class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        count = s.count("0")
        i = sm = 0
        
        for c in s[::-1]:
            if c == "1":
                sm += 1<<i
                if sm<=k:
                    count += 1
                else:
                    break
            i += 1
        
        return count 
