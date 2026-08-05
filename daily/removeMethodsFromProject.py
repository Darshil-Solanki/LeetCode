class Solution:
    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        in_degree = [0]*n
        for u, v in invocations:
            graph[u].append(v)
            in_degree[v] += 1
        
        sus_methods = [False]*n
        queue = deque([k])
        sus_methods[k] = True

        while queue:
            u = queue.popleft()
            for v in graph[u]:
                in_degree[v] -= 1
                if not sus_methods[v]:
                    queue.append(v)
                    sus_methods[v] = True
        
        can_remove = True
        for i in range(n):
            if sus_methods[i] and in_degree[i]>0:
                can_remove = False
                break
        
        if not can_remove:
            return list(range(n))
        
        return [i for i in range(n) if not sus_methods[i]]
        
