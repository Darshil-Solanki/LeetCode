class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        MOD = 1_000_000_007

        graph = defaultdict(list)
        for u, v, weight in roads:
            graph[u].append((v, weight))
            graph[v].append((u, weight))

        distances = [float("inf")]*n
        path_count = [0]*n
        distances[0] = 0
        heap = [(0, 0)]
        path_count[0] = 1

        while heap:
            curr_dist, node = heappop(heap)
            if curr_dist>distances[node]: continue

            for nei, weight in graph[node]:
                new_dist = curr_dist+weight
                if new_dist<distances[nei]:
                    distances[nei] = new_dist
                    path_count[nei] = path_count[node]
                    heappush(heap, (new_dist, nei))
                elif new_dist==distances[nei]:
                    path_count[nei]= (path_count[nei]+path_count[node])%MOD
        
        return path_count[n-1]
        
        # @cache
        # def dp(node, time):
        #     if node==0:
        #         if time == 0: return 1
        #         return 0
        #     ans = 0
        #     for nei, weight in graph[node]:
        #         if not visited[nei]:
        #             visited[nei] = True
        #             ans += dp(nei, time-weight)%MOD
        #             visited[nei] = False
            
        #     return ans%MOD

        # visited = [False]*n
        # return dp(n-1, distances[n-1])
