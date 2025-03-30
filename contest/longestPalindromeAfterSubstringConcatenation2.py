class Solution:
    def longestPalindrome(self, s: str, t: str) -> int:
        m, n = len(s), len(t)
        
        def longest_palindrome_starting_from(st, i):
            ans = 1
            for right in range(len(st)-1, i, -1):
                left, tempR = i, right
                while left<tempR and st[left] == st[tempR]:
                    left += 1
                    tempR -= 1
                if left >= tempR:
                    ans = max(ans, right - i + 1)
                    break
            return ans

        def longest_palindrome_ending_at(st, j):
            ans = 1
            for left in range(j):
                tempL, right = left, j
                while tempL<right and st[tempL] == st[right]:
                    tempL += 1
                    right -= 1
                if tempL >= right:
                    ans = max(ans, j-left + 1)
                    break
            return ans

        p = [0] * m
        for i in range(m):
            p[i] = longest_palindrome_starting_from(s, i)

        q = [0] * n
        for j in range(n):
            q[j] = longest_palindrome_ending_at(t, j)
        ans = 0

        dp = [[0] * (n) for _ in range(m)]
        for i in range(m-1, -1, -1):
            for j in range(n):
                longest_alone =  max(p[i], q[j])
                if s[i] != t[j]:
                    dp[i][j] = longest_alone
                else:
                    with_new_2 = 2
                    if i+1<m and j>0:
                        with_new_2 = max(with_new_2, 2+dp[i+1][j-1])
                    if i+1<m:
                        with_new_2 = max(with_new_2, 2+p[i+1])
                    if j>0:
                        with_new_2 = max(with_new_2, 2+q[j-1])
                    dp[i][j] = max(longest_alone, with_new_2)
                ans = max(ans, dp[i][j])

        return ans
