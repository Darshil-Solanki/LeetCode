class Solution:
    def countCommas(self, n: int) -> int:
        ans = 0
        if n>999_999_999_999_999:
            ans = 5
            n-=1
        if n>999_999_999_999:
            ans += (n-999_999_999_999)*4
            n = 999_999_999_999
        if n>999_999_999:
            ans += (n-999_999_999)*3
            n = 999_999_999
        if n>999_999:
            ans += (n-999_999)*2
            n = 999_999
        if n>999:
            ans += n-999
        return ans
