class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        n = len(colors)
        graph = defaultdict(list)

        for u, v in edges:
            graph[u].append(v)

        def dfs(node):
            nonlocal ans
            if visited_mark[node] == 1: return None
            if visited_mark[node] == 2: return memo[node]

            visited_mark[node] = 1
            color_counts = [0]*26
        
            for nei in graph[node]:
                temp_result = dfs(nei)
                if temp_result is None: return None
                for c in range(26):
                    color_counts[c] = max(color_counts[c], temp_result[c])
            
            node_color = ord(colors[node])-97
            color_counts[node_color] += 1
            visited_mark[node] = 2
            ans = max(ans, color_counts[node_color])
            memo[node] = color_counts
            return color_counts

        ans = -1
        visited_mark = [0]*n
        memo = [None]*n
        for node in range(n):
            if not visited_mark[node]:
                if dfs(node) is None: return -1

        
        return ans


    # from chatgpt topo with dp 
    # def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
    #     n = len(colors)
    #     graph = defaultdict(list)
    #     indegree = [0] * n

    #     for u, v in edges:
    #         graph[u].append(v)
    #         indegree[v] += 1

    #     # Topological sort to detect cycles
    #     queue = deque([i for i in range(n) if indegree[i] == 0])
    #     topo_order = []
    #     while queue:
    #         node = queue.popleft()
    #         topo_order.append(node)
    #         for nei in graph[node]:
    #             indegree[nei] -= 1
    #             if indegree[nei] == 0:
    #                 queue.append(nei)

    #     if len(topo_order) < n:
    #         return -1  # There is a cycle

    #     # DP: dp[node][c] = max count of color c (0-25) along any path ending at node
    #     dp = [[0] * 26 for _ in range(n)]

    #     for node in topo_order:
    #         color_index = ord(colors[node]) - ord('a')
    #         dp[node][color_index] += 1
    #         for nei in graph[node]:
    #             for c in range(26):
    #                 dp[nei][c] = max(dp[nei][c], dp[node][c])

    #     return max(max(row) for row in dp)
