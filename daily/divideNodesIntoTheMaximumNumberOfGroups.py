class Solution:
    def magnificentSets(self, n: int, edges: List[List[int]]) -> int:
        
        # with help for hint and solution by rahulvijayan2291/
        graph = [[] for _ in range(n+1)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        # Check if graph is bipartite using color
        def bipartite(graph, n):
            color = [0]*(n+1)

            def bfs_check_bipartite(node):
                queue = deque([node])
                color[node]=1
                while queue:
                    curr = queue.popleft()
                    curr_color = 2 if color[curr]==1 else 1
                    for nei in graph[curr]:
                        if color[nei]==0:
                            color[nei] = curr_color
                            queue.append(nei)
                        elif color[nei]!=curr_color:
                            return False
                return True

            for i in range(1, n+1):
                if color[i]==0 and not bfs_check_bipartite(i):
                    return False
            return True

        if not bipartite(graph, n):
            return -1
        
        # Find Maximum BFS Depth for each node
        bfs_depth = [0]*(n+1)
        for i in range(1, n+1):
            queue = deque([(i, 1)])
            seen = [0]*len(graph)
            seen[i] = 1
            last_depth = 1
            while queue:
                curr, depth = queue.popleft()
                last_depth = depth
                for nei in graph[curr]:
                    if not seen[nei]:
                        seen[nei]=1
                        queue.append((nei, depth+1))
            bfs_depth[i] = last_depth
        
        # Finding maximum depth in each connected components and summing up all connected components max depth to find total groups
        seen = set()
        def dfs(node):
            max_depth = bfs_depth[node]
            for nei in graph[node]:
                if nei not in seen:
                    seen.add(nei)
                    max_depth = max(max_depth, dfs(nei))
            return max_depth

        total_groups = 0
        for i in range(1, n+1):
            if i not in seen:
                seen.add(i)
                total_groups+=dfs(i)
        return total_groups
