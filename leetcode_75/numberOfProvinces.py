class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        
        def dfs(i):
            isConnected[i][i] = 0
            for j in range(n):
                if isConnected[j][j] and isConnected[i][j]:
                    dfs(j)
        
        ans = 0
        for i in range(n):
            if isConnected[i][i]:
                ans+=1
                dfs(i)
        return ans
        
        # copied from submission
        # n = len(isConnected)
        # visited = [0] * n
        # count = 0

        # def dfs(node):
        #     visited[node] = 1
        #     for i in range(len(isConnected[node])):
        #         if isConnected[node][i] == 1 and not visited[i]:
        #             dfs(i)

        # for i in range(n):
        #     if not visited[i]:
        #         count += 1
        #         dfs(i)
        # return count
