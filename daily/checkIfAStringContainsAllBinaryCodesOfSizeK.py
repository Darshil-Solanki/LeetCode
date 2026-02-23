class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        if len(s) - k + 1 < (1<<k):
            return False
        code_set = set()        
        for i in range(len(s)-k+1):
            code_set.add(s[i:i+k])
        
        return len(code_set) == 2**k
