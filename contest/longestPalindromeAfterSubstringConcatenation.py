class Solution:
    def longestPalindrome(self, s: str, t: str) -> int:
        ans = 0
        def is_palindrome(st):
            return st==st[::-1]
            
        def longestPalindromeLength(st):
            ans = 0
            for i in range(len(st)):
                left = right = i
                while left>-1 and right<len(st) and st[left]==st[right]:
                    ans = max(ans, right-left+1)
                    left-=1
                    right+=1
                    
                left, right = i, i+1
                while left>-1 and right<len(st) and st[left]==st[right]:
                    ans = max(ans, right-left+1)
                    left-=1
                    right+=1
            return ans
        ans = max(longestPalindromeLength(s), longestPalindromeLength(t))
        for i in range(len(s)):
            for j in range(i+1, len(s)+1):
                curr_s = s[i:j]
                for k in range(len(t)):
                    for l in range(k+1, len(t)+1):
                        new_str = "".join([curr_s, t[k:l]])
                        if is_palindrome(new_str):
                            ans = max(ans, len(new_str))

        return ans
