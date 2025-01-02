class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        queue = deque([(0, rooms[0])])
        seen = {0}
        n = len(rooms)
        while queue:
            node, keys = queue.popleft()
            if len(seen)==n: return True
            for nei in keys:
                if nei not in seen:
                    seen.add(nei)
                    queue.append((nei, rooms[nei]))
        return False

        # faster method
        # visited = set()
        # def dfs(node):
        #     visited.add(node)
        #     if not rooms[node]:
        #         return
            
        #     for i in rooms[node]:
        #         if i not in visited:
        #             dfs(i)
        # dfs(0)
        # return len(visited) == len(rooms)
