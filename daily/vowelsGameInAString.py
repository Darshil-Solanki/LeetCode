class Solution:
    def doesAliceWin(self, s: str) -> bool:
        vowel = set(["a", "e", "i", "o", "u"])
        
        for c in s:
            if c in vowel:
                return True
        
        return False
