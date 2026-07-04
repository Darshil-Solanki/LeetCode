class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        graph = defaultdict(list)

        for u, v, dist in roads:
            graph[u].append((v, dist))
            graph[v].append((u, dist))
        
        seen = [False]*(n+1)
        seen[1] = True
        queue = deque([1])

        ans = float("inf")

        while queue:
            node = queue.popleft()
            for nei, nei_dist in graph[node]:
                ans = min(ans, nei_dist)
                if not seen[nei]:
                    seen[nei] = True
                    queue.append(nei)
        
        return ans
