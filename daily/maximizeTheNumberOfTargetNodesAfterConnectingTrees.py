class Solution:
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]], k: int) -> List[int]:
        n, m = len(edges1)+1, len(edges2)+1
        graph1 = [[] for _ in range(n)]
        graph2 = [[] for _ in range(m)]

        for u, v in edges1:
            graph1[u].append(v)
            graph1[v].append(u)
        
        for u, v in edges2:
            graph2[u].append(v)
            graph2[v].append(u)
        
        def dfs(graph, node, parent, k):
            if k<0: return 0

            graph_val = graph
            graph = graph1 if graph==1 else graph2
            ans = 1
            
            for nei in graph[node]:
                if nei==parent: continue
                ans += dfs(graph_val, nei, node, k-1)
            
            return ans


        count = [0]*m
        for node in range(m):
            count[node] = dfs(2, node, -1, k-1)
        max_count2 = max(count)

        count = [0]*n
        for node in range(n):
            count[node] = dfs(1, node, -1, k) + max_count2
        
        return count
