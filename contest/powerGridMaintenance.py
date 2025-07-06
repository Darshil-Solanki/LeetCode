class DSU:
    def __init__(self, n):
        self.parent = list(range(n+1))
    
    def find(self, node):
        if self.parent[node] != node:
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]
    
    def union(self, u, v):
        self.parent[self.find(u)] = self.find(v)

class Solution:
    def processQueries(self, c: int, connections: List[List[int]], queries: List[List[int]]) -> List[int]:
        dsu = DSU(c)
        for u, v in connections:
            dsu.union(u, v)

        components = defaultdict(list)
        for station in range(1, c+1):
            root = dsu.find(station)
            components[root].append(station)
        
        for root, children in components.items():
            components[root] = SortedSet(children)
        
        ans = []
        for qtype, station in queries:
            root = dsu.find(station)
            online_set = components[root]
            if qtype == 1:
                if station in online_set:
                    ans.append(station)
                elif online_set:
                    ans.append(online_set[0])
                else:
                    ans.append(-1)
            else:
                if station in online_set:
                    online_set.remove(station)

        return ans

        
