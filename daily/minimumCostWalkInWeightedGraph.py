class Solution:
    def minimumCost(self, n: int, edges: List[List[int]], query: List[List[int]]) -> List[int]:
        graph = defaultdict(list)

        for u, v, weight in edges:
            graph[u].append((v, weight))
            graph[v].append((u, weight))
        
        seen = [False]*n
        def dfs(node):
            connected_components[node]=connected_components_id
            ans = -1
            for nei, weight in graph[node]:
                ans &= weight
                if not seen[nei]:
                    seen[nei]=True
                    ans &= dfs(nei)
            return ans
                    
        connected_components = [-1]*n
        min_cost_components = []
        connected_components_id = 0
        for node in range(n):
            if not seen[node]:
                seen[node] = True
                min_cost_components.append(dfs(node))
                connected_components_id+=1
    
        ans = []
        for start, end in query:
            if connected_components[start]==connected_components[end]:
                ans.append(min_cost_components[connected_components[start]])
            else:
                ans.append(-1)
        
        return ans
