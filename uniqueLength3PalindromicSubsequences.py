class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        letters = set(s)
        ans = 0

        for letter in letters:
            l, r = s.index(letter), s.rindex(letter)
            between = set(s[l+1:r])
            ans += len(between)
        
        return ans

        # one liner
        # return sum(len(set(s[s.index(letter)+1:s.rindex(letter)]))for letter in letters )
