class Solution:
    def minTime(self, n: int, edges: List[List[int]], k: int) -> int:
        graph = defaultdict(list)
        maxTime = 0
        for u, v, time in edges:
            graph[u].append((v, time))
            graph[v].append((u, time))
            maxTime = max(maxTime, time)

        def dfs(node, t, seen):
            for nei, time in graph[node]:
                if nei not in seen:
                    if time<=t:
                        continue
                    seen.add(nei)
                    dfs(nei, t, seen)
            
                   
        def check(time):
            seen = set()
            comp = 0
            for node in range(n):
                if node in seen:
                    continue
                seen.add(node)
                comp += 1
                dfs(node, time, seen)
                
            return comp>=k

        # already k component exist
        if check(0):
            return 0
        
        left, right = 1, maxTime
        while left<=right:
            mid = (left+right)//2
            if check(mid):
                ans = mid
                right = mid - 1
            else:
                left = mid + 1

        return ans
