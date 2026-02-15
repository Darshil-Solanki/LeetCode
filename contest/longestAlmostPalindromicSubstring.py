class Solution:
    def almostPalindromic(self, s: str) -> int:
        n = len(s)
        self.ans = 2

        def dp(left, right, used):
            if left>-1 and right<n:
                if s[left]==s[right]:
                    self.ans = max(self.ans, right-left+1)
                    dp(left-1, right+1, used)
                elif s[left]!=s[right] and not used:
                    self.ans = max(self.ans, right-left)
                    if left-1>-1 and s[left-1]==s[right]:
                        dp(left-1, right, True)
                    if right+1<n and s[right+1]==s[left]:
                        dp(left, right+1, True)
            elif left>-1 and right==n and not used:
                self.ans = max(self.ans, right-left)
            elif right<n and left==-1 and not used:
                self.ans = max(self.ans, right+1)
            
        for i in range(1, n):
            dp(i, i, False)
            if s[i]==s[i-1]:
                dp(i-1, i, False)
        
        return self.ans
