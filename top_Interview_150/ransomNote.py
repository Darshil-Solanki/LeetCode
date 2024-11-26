from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransomCount = Counter(ransomNote)
        magazineCount = Counter(magazine)
        for key,value in ransomCount.items():
            try:
                if magazineCount.get(key)<value:
                    return False                    
            except:
                return False
        return True
