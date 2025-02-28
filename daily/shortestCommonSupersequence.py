class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        s1_len, s2_len = len(str1), len(str2)

        dp = [[0]*(s2_len+1) for _ in range(s1_len+1)]

        for row in range(s1_len+1):
            dp[row][0] = row
        
        for col in range(s2_len+1):
            dp[0][col] = col
        
        for row in range(1, s1_len+1):
            for col in range(1, s2_len+1):
                if str1[row-1]==str2[col-1]:
                    dp[row][col]=dp[row-1][col-1]+1
                else:
                    dp[row][col]=min(dp[row-1][col], dp[row][col-1])+1

        ans = []
        row, col = s1_len, s2_len
        while row>0 and col>0:
            if str1[row-1]==str2[col-1]:
                ans.append(str1[row-1])
                row-=1
                col-=1
            elif dp[row-1][col]<dp[row][col-1]:
                ans.append(str1[row-1])
                row-=1
            else:
                ans.append(str2[col-1])
                col-=1

        while row>0:
            ans.append(str1[row-1])
            row-=1
            
        while col>0:
            ans.append(str2[col-1])
            col-=1

        return "".join(ans[::-1])

        # Similar bottom up approach but more cleaner and little bit faster due use of string instead of array at end
        # n = len(str1)
        # m = len(str2)
        # memo = [[0] * (m + 1) for _ in range(n + 1)]

        # for i in range(n - 1, -1, -1):
        #     for j in range(m - 1, -1, -1):
        #         if str1[i] == str2[j]:
        #             memo[i][j] = memo[i + 1][j + 1] + 1
        #         else:
        #             if memo[i + 1][j] > memo[i][j + 1]:
        #                 memo[i][j] = memo[i + 1][j]
        #             else:
        #                 memo[i][j] = memo[i][j + 1]

        # res: str = ""
        # i = 0
        # j = 0

        # while i < n and j < m:
        #     if str1[i] == str2[j]:
        #         res += str1[i]
        #         i += 1
        #         j += 1
        #     elif memo[i + 1][j] >= memo[i][j + 1]:
        #         res += str1[i]
        #         i += 1
        #     else:
        #         res += str2[j]
        #         j += 1

        # if j < m:
        #     res += str2[j:]
        # if i < n:
        #     res += str1[i:]

        # return res
