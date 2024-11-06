class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        if not word1: return len(word2)
        if not word2: return len(word1)
        dp = [[0]*(len(word2)) for i in range(len(word1))]
        for i in range(len(word1), 0, -1):
            dp[len(word1)-i].append(i)
        dp.append([ i for i in range(len(word2), -1 , -1)])

        for i in range(len(word1)-1, -1, -1):
            for j in range(len(word2)-1, -1, -1):
                if word1[i]==word2[j]:
                    dp[i][j]=dp[i+1][j+1]
                else:
                    dp[i][j]=1+min(dp[i+1][j], dp[i][j+1], dp[i+1][j+1])
        return dp[0][0] 
        
        # Better way to reduce runtime(by avoiding time to create dp table) using bfs
        # return bfs(word1, word2)
        
        # def bfs(self, word1, word2):
        #     m, n = len(word1), len(word2)
        #     q = deque([(0, 0)])
        #     numEdits = 0
        #     visited = set()
        #     while q:
        #         qLen = len(q)
        #         for _ in range(qLen):
        #             i, j = q.popleft()
        #             if (i,j) in visited:
        #                 continue
        #             visited.add((i,j))

        #             while i < m and j < n and word1[i] == word2[j]:
        #                 i += 1
        #                 j += 1

        #             if i == m and j == n:
        #                 return numEdits
                    
        #             q.append((i+1, j)) # delete
        #             q.append((i+1,j+1)) # replace
        #             q.append((i,j+1)) # insert
        #         numEdits += 1
            
        #     return -1
        # def dfs(self, i1, word1, m, i2, word2, n, memo):
        #     if i1 == m and i2 == n:
        #         return 0
        #     if i1 == m:
        #         return n - i2
        #     if i2 == n:
        #         return m - i1
        #     if (i1, i2) in memo:
        #         return memo[(i1, i2)]

        #     res = float("inf")
        #     if word1[i1] == word2[i2]:
        #         res = self.dfs(i1+1, word1, m, i2+1, word2, n, memo)
        #     else:
        #         insert = self.dfs(i1, word1, m, i2+1, word2, n, memo)
        #         delete = self.dfs(i1+1, word1, m, i2, word2, n, memo)
        #         replace = self.dfs(i1+1, word1, m, i2+1, word2, n, memo)
        #         res = min(insert, delete, replace) + 1
        #     memo[(i1, i2)] = res

        #     return memo[(i1, i2)]

        
