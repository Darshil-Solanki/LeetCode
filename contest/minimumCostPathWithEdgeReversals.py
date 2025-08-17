class Solution:
    def minCost(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for u, v, w in edges:
            graph[u].append((v, w))
            graph[v].append((u, 2*w))

        min_cost = [float("inf")]*n
        min_cost[0] = 0
        heap = [(0, 0)]

        while heap:
            curr_cost, node = heappop(heap)

            if node==n-1:
                return curr_cost
            if curr_cost>min_cost[node]:
                continue
            
            for nei, cost in graph[node]:
                new_cost = curr_cost+cost
                if new_cost<min_cost[nei]:
                    min_cost[nei] = new_cost
                    heappush(heap, (new_cost, nei))
        
        return -1
