class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        word_set = set(word)
        ans = 0
        for c in "abcdefghijklmnopqrstuvwxyz":
            if c in word_set and c.upper() in word_set:
                ans += 1
        return ans
