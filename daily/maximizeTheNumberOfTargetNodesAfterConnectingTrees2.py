class Solution:
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]]) -> List[int]:
        def dfs(graph, node, parent, depth, color):
            ans = 1 - depth % 2
            color[node] = depth % 2
            
            for nei in graph[node]:
                if nei == parent: continue
                ans += dfs(graph, nei, node, depth+1, color)
            
            return ans

        n = len(edges1) + 1
        m = len(edges2) + 1
        color1 = [0]*n
        color2 = [0]*m
        graph1 = defaultdict(list)
        graph2 = defaultdict(list)

        for u, v in edges1:
            graph1[u].append(v)
            graph1[v].append(u)
        for u, v in edges2:
            graph2[u].append(v)
            graph2[v].append(u)

        count1 = dfs(graph1, 0, -1, 0, color1)
        count2 = dfs(graph2, 0, -1, 0, color2)

        count1 = [count1, n-count1]
        count2 = [count2, m-count2]

        ans = [0]*n
        max_count2 = max(count2[0], count2[1])
        for i in range(n):
            ans[i] = count1[color1[i]] + max_count2
        
        return ans
