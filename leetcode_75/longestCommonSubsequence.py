class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        dp = [[0]*(n+1) for i in range(m+1)]
        
        for i in range(1, m+1):
            for j in range(1, n+1):
                dp[i][j] = dp[i-1][j-1]+1 if text1[i-1]==text2[j-1] else max(dp[i-1][j], dp[i][j-1])

        return dp[m][n]

        # faster method from submission
        # common_chars = set(text1) & set(text2)
        
        # filtered_texts_1 = []
        # filtered_texts_2 = []
        
        # text1_len = len(text1)
        # text2_len = len(text2)

        # max_len  = max(text1_len, text2_len)

        # for i in range(max_len):
        #     if i <= text1_len - 1:
        #         if text1[i] in common_chars:
        #             filtered_texts_1.append(text1[i])
        #     if i <= text2_len - 1:
        #         if text2[i] in common_chars:
        #             filtered_texts_2.append(text2[i])


        # if filtered_texts_1 == filtered_texts_2:
        #     return len(filtered_texts_1)
        # else:
        #     dp = [0] * len(filtered_texts_2)
        #     for ch in filtered_texts_1:
        #         highest_score = 0
        #         for i in range(len(filtered_texts_2)):
        #             if dp[i] > highest_score:
        #                 highest_score = dp[i]
        #             elif ch == filtered_texts_2[i]:
        #                 dp[i] = highest_score + 1      
        #     if dp:
        #         return max(dp)
            
        # return 0
