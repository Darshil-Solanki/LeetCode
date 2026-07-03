class Solution:
    def findMaxPathScore(self, edges: List[List[int]], online: List[bool], k: int) -> int:
        if not edges:
            return -1
        n = len(online)
        graph = defaultdict(list)
        left = right = edges[0][2]
        for u, v, c in edges:
            if not online[u] or not online[v]:
                continue
            graph[u].append((v, c))
            left = min(left, c)
            right = max(right, c)
        
        def check(min_thr_cost):
            min_cost = [float("inf")]*n
            queue = [(0, 0)]
            min_cost[0] = 0
            while queue:
                cost, node = heappop(queue)
                if cost>k:
                    return False
                if node == n-1:
                    return True
                if cost>min_cost[node]:
                    continue
                
                for nei, nei_cost in graph[node]:
                    if nei_cost<min_thr_cost:
                        continue
                    if min_cost[node]+nei_cost < min_cost[nei]:
                        min_cost[nei] = min_cost[node]+nei_cost
                        heappush(queue, (min_cost[nei], nei))
            return False
        
        if not check(left):
            return -1
        
        ans = -1
        while left<=right:
            mid = (left+right)//2
            if check(mid):
                ans = mid
                left = mid+1
            else:
                right = mid-1
        
        return right
