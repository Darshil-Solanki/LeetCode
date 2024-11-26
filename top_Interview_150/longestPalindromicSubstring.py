class Solution:
    def longestPalindrome(self, s: str) -> str:
        res_l, res_r = 0, 0
        maxLen = 0
        def getPalindrome(l, r):
            while -1<l and r<len(s) and s[l]==s[r]:
                nonlocal maxLen, res_l, res_r
                if r-l+1 > maxLen:
                    maxLen = r-l+1
                    res_l = l; res_r = r
                l-=1
                r+=1
        for i in range(len(s)):
            # for odd length
            l, r = i, i
            getPalindrome(l,r)

            # for even length
            l, r = i, i+1
            getPalindrome(l, r)
        return s[res_l:res_r+1]
