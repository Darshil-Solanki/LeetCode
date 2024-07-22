class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        patternHash, wordHash= {}, {}
        words = s.split()
        if len(words)!=len(pattern):
            return False
        for i in range(len(pattern)):
            if patternHash.get(pattern[i])==None and words[i] not in patternHash.values():
                patternHash[pattern[i]]=words[i]
            if patternHash.get(pattern[i])!=words[i]:
                return False
        return True
        
        
