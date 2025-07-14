class Solution:
    def minCost(self, n: int, edges: List[List[int]], k: int) -> int:
        if k>=n: return 0
        edges.sort(key = lambda x: x[2])
        parent = list(range(n))
        component_size = [1]*n

        def get_root(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x 
        
        components = n
        for u, v, w in edges:
            ru, rv = get_root(u), get_root(v)
            if ru!=rv:
                if component_size[ru]<component_size[rv]:
                    ru, rv = rv, ru
                parent[rv] = ru
                component_size[ru] += component_size[rv]
                components -= 1
                if components <= k:
                    return w


        # from contest dfs in graph,  status: TLE 
        # edges.sort(key = lambda x: -x[2])
        # graph = defaultdict(set)
        # ans = 0
        
        # for u, v, w in edges:
        #     graph[u].add((v, w))
        #     graph[v].add((u, w))
        #     ans = max(ans, w)
        
        # def get_component_count_and_weight():
        #     visited = [False]*n
        #     max_weight = 0
        #     def dfs(node):
        #         weight = 0
        #         for nei, w in graph[node]:
        #             if not visited[nei]:
        #                 visited[nei] = True
        #                 weight = max(dfs(nei), weight, w)
        #         return weight
                        
        #     count = 0
        #     for node in range(n):
        #         if not visited[node]:
        #             visited[node] = True
        #             max_weight = max(max_weight, dfs(node))
        #             count+=1
        #     return count, max_weight

        # for i, (u, v, w) in enumerate(edges):
        #     graph[u].remove((v, w))
        #     graph[v].remove((u, w))
        #     component, max_weight = get_component_count_and_weight()
            
        #     if component<=k:
        #         ans = min(ans, max_weight)
        #     else:                
        #         break
            
        # return ans
