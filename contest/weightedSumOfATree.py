class Solution:
    def weightedSum(self, parent: list[int], nums: list[int]) -> int:
        graph = defaultdict(list)
        n = len(parent)
        for v in range(1, n):
            graph[parent[v]].append(v)

        height = 0
        queue = deque([0])
        while queue:
            height += 1
            for _ in range(len(queue)):
                node = queue.popleft()
                for child in graph[node]:
                    queue.append(child)

        queue = deque([0])
        tot, depth = 0, 0
        while queue:
            depth += 1
            for _ in range(len(queue)):
                node = queue.popleft()
                tot += nums[node] * (height - depth + 1)
    
                for child in graph[node]:
                    queue.append(child)
                    
        return tot
        
        
