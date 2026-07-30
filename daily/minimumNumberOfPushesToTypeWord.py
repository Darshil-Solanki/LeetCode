class Solution:
    def minimumPushes(self, word: str) -> int:
        n = len(word)
        if n<9:
            return n
        if n<17:
            return 2*n - 8
        if n<25:
            return 3*n - 24
        return 4*n - 48
