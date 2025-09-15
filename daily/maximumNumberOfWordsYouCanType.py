class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        words = text.split(" ")
        return sum( all(c not in brokenLetters for c in word)  for word in words)
