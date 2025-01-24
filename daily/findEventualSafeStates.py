class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        seen = [0]*n
        res = []
        def dfs(node):
            if seen[node]==2: return True
            if seen[node]: return False
            seen[node] = 1
            for nei in graph[node]:
                if not dfs(nei): return False
            seen[node]=2
            res.append(node)
            return True
        for i in range(n):
            if not seen[i]:
                dfs(i)
        res.sort()
        return res

        # BFS way from submitted
        # n = len(graph)
        # ultagraph = [[] for _ in range(n)]
        # outdegree = [0] * n
        # ans = []

        # for i in range(n):
        #     for neighbor in graph[i]:
        #         ultagraph[neighbor].append(i)
        #         outdegree[i] += 1

        # q = deque()
        # for i in range(n):
        #     if outdegree[i] == 0:
        #         q.append(i)

        # while q:
        #     node = q.popleft()
        #     ans.append(node)

        #     for neighbor in ultagraph[node]:
        #         outdegree[neighbor] -= 1
        #         if outdegree[neighbor] == 0:
        #             q.append(neighbor)

        # ans.sort()
        # return ans
