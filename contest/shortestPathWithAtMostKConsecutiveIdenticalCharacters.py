class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], labels: str, k: int) -> int:
        if n==1:
            return 0
        graph = defaultdict(list)
        for u, v, w in edges:
            graph[u].append((v, w))
        
        dist = [[float("inf")]*(k+1) for _ in range(n)]
        dist[0][1] = 0

        queue = [(0, 0, 1)]
        while queue:
            cost, u, cons = heappop(queue)
            if cost != dist[u][cons]:
                continue
            if u == n-1:
                return cost
                
            for v, w in graph[u]:
                if labels[u]==labels[v]:
                    next_cons = cons+1
                else:
                    next_cons = 1

                if next_cons > k:
                    continue
                next_cost = cost+w
                if next_cost<dist[v][next_cons]:
                    dist[v][next_cons] = next_cost
                    heappush(queue, (next_cost, v, next_cons))

        return -1
