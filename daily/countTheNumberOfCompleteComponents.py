class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:

        graph = [[] for i in range(n)]

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)


        def dfs(node, component):
            component.append(node)
            for nei in graph[node]:
                if not visited[nei]:
                    visited[nei]=True
                    dfs(nei, component)


        visited = [False]*n
        ans = 0
        for node in range(n):
            if not visited[node]:
                visited[node] = True
                
                component = []
                dfs(node, component)
                for u in component:
                    if len(graph[u])!=len(component)-1:
                        break
                else:
                    ans+=1
        
        return ans
