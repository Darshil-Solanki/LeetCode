class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        adjacencyList = collections.defaultdict(list)
        for i, eq in enumerate(equations):
            a, b = eq
            adjacencyList[a].append([b, values[i]])
            adjacencyList[b].append([a, 1/values[i]])
        
        def dfs(a, b):
            if a not in adjacencyList or b not in adjacencyList:
                return -1
            if a == b:
                return 1
            seen.add(a)
            for nei, neiWeight in adjacencyList[a]:
                if nei not in seen:
                    result = dfs(nei, b)
                    if result != -1:  # If we found a valid path
                        return result * neiWeight

            return -1

        res = []
        for a, b in queries:
            seen = set()
            res.append(dfs(a,b))
        return res
    
    # BFS way
    # def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
    #     adjacencyList = collections.defaultdict(list)
    #     for i, eq in enumerate(equations):
    #         a, b = eq
    #         adjacencyList[a].append([b, values[i]])
    #         adjacencyList[b].append([a, 1/values[i]])
        
    #     def bfs(a, b):
    #         if a not in adjacencyList or b not in adjacencyList:
    #             return -1
    #         if a == b:
    #             return 1
    #         seen = set()
    #         seen.add(a)
    #         queue = [(a, 1)]
    #         while queue:
    #             node, curWeight = queue.pop(0)
    #             for nei, neiWeight in adjacencyList[node]:
    #                 if nei not in seen:
    #                     if b==nei:
    #                         return curWeight*neiWeight
    #                     seen.add(nei)
    #                     queue.append((nei, curWeight*neiWeight))
    #         return -1
    #     return [bfs(a, b)  for a, b in queries]
