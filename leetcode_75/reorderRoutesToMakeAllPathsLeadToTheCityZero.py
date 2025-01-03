class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        graph = defaultdict(list)
        for a, b in connections:
            graph[a].append((b, True))
            graph[b].append((a, False))
        ans = 0
        seen = {0}
        stack = [0]
        while stack:
            node = stack.pop()
            for nei, status in graph[node]:
                if nei not in seen:
                    seen.add(nei)
                    stack.append(nei)
                    if status: ans+=1
        return ans
        
        # copied form submission
        # seen = set()
        # seen.add(0)
        # count = 0
        # while len(seen)<n:
        #     check = []
        #     for path in connections:
        #         if path[1] in seen:
        #             seen.add(path[0])
        #         elif path[0] in seen:
        #             seen.add(path[1])
        #             count += 1
        #         else:
        #             check.append(path)
        #     connections = check[::-1]
        # return count
