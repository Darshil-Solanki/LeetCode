class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        meetings.sort(key=lambda x: (x[2], x[0], x[1]))
        meetings = groupby(meetings, key=lambda x: x[2])
        
        graph = UnionFind(n)
        graph.unite(firstPerson, 0)
        
        for time, same_time_meetings in meetings:
            same_time_meetings = list(same_time_meetings)
            for (x, y, t) in same_time_meetings:
                graph.unite(x, y)

            for (x, y, t) in same_time_meetings:
                if not graph.connected(x, 0):
                    graph.reset(x)
                    graph.reset(y)
        
        return [i for i in range(n) if graph.connected(i, 0)]

class UnionFind:
    def __init__(self, nodes: int):
        # Initialize parent and rank arrays
        self.parent = [i for i in range(nodes)]
        self.rank = [0] * nodes

    def find(self, x: int) -> int:
        # Find the parent of node x. Use Path Compression
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def unite(self, x: int, y: int) -> None:
        # Unite two nodes x and y, if they are not already united
        px = self.find(x)
        py = self.find(y)
        if px != py:
            # Union by Rank Heuristic
            if self.rank[px] > self.rank[py]:
                self.parent[py] = px
            elif self.rank[px] < self.rank[py]:
                self.parent[px] = py
            else:
                self.parent[py] = px
                self.rank[px] += 1

    def connected(self, x: int, y: int) -> bool:
        # Check if two nodes x and y are connected or not
        return self.find(x) == self.find(y)

    def reset(self, x: int) -> None:
        # Reset the initial properties of node x
        self.parent[x] = x
        self.rank[x] = 0
