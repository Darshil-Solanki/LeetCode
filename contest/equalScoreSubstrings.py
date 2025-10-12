class Solution:
    def scoreBalance(self, s: str) -> bool:
        left_prefix, right_prefix = [], []
        t, n = 0, len(s)
        for c in s:
            t += ord(c)-96
            left_prefix.append(t)
        t = 0
        for c in s[::-1]:
            t += ord(c)-96
            right_prefix.append(t)
        right_prefix = right_prefix[::-1]
        
        for i in range(n-1):
            left = left_prefix[i]
            right = right_prefix[i+1]
            if left == right:
                return True

        return False
