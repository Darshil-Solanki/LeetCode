class Solution:
    def assignEdgeWeights(self, edges: List[List[int]]) -> int:
        n = len(edges)+1
        MOD = 1_000_000_007
        graph = defaultdict(list)

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        queue = deque([1])
        leaf_nodes = []
        seen = [False]*(n+1)
        seen[0] = seen[1] = True
        depth = 0
        while queue:
            leaf_nodes = queue.copy()
            for _ in range(len(queue)):
                node = queue.popleft()
                for nei in graph[node]:
                    if not seen[nei]:
                        seen[nei] = True
                        queue.append(nei)
            depth += 1
        
        return pow(2, depth-2, MOD)
