class Solution:
    def baseUnitConversions(self, conversions: List[List[int]]) -> List[int]:
        n = len(conversions)
        res = [0]*(n+1)
        res[0] = 1
        graph = defaultdict(list)
        MOD = 1_000_000_007
        
        for u, v, weight in conversions:
            graph[u].append((v, weight))

        stack = [(0, 1)]
        while stack:
            node, curr_unit = stack.pop()
            for nei, weight in graph[node]:
                res[nei] = (curr_unit*weight)%MOD
                stack.append((nei, (curr_unit*weight)%MOD))

        return res
