class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        result = [s[i:i+k] for i in range(0, len(s), k)]        
        result[-1] = result[-1].ljust(k, fill)
        return result
