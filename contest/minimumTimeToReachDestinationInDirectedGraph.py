class Solution:
    def minTime(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        
        for u, v, start, end in edges:
            graph[u].append((v, (start, end)))
        
        min_time = [float("inf")]*n
        queue = deque([(0, 0)])
        
        while queue:
            node, curr_time = queue.popleft()
            if curr_time>=min_time[node]:
                continue
            
            min_time[node] = curr_time

            for nei, (start, end) in graph[node]:
                if curr_time>end:
                    continue
                new_time = curr_time
                if curr_time<start:
                    new_time = start

                if new_time+1<min_time[nei]:
                    queue.append((nei, new_time+1))

        return -1 if min_time[n-1] == float("inf") else min_time[n-1]
