class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        self.ans = 0
        graph = [[] for _ in range(n)]
        
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        def dfs(curr, parent):
            tot = 0

            for nei in graph[curr]:
                if nei != parent:
                    tot += dfs(nei, curr)
                    tot %= k
            
            tot += values[curr]
            tot %= k

            if tot == 0:
                self.ans += 1
            
            return tot

        dfs(0, -1)
        return self.ans
