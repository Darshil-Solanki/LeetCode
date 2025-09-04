class Solution:
    def maxWeight(self, n: int, edges: List[List[int]], k: int, t: int) -> int:
        graph = defaultdict(list)

        for u, v, w in edges:
            graph[u].append((v,w))
            
        @cache
        def dfs(node, curr, remaining):
            if remaining==0:
                return curr
            ans = -1
            for nei, weight in graph[node]:
                if curr+weight>=t:
                    continue
                ans = max(ans, dfs(nei, curr+weight, remaining-1))
            return ans

        ans = -1
        for node in range(n):
            ans = max(ans, dfs(node, 0, k))
        
        return ans
