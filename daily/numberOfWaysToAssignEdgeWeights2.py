class LCA:
    def __init__(self, edges, root):
        self.n = len(edges) + 1
        self.m = int(log2(self.n)) + 2
        self.e = [[] for _ in range(self.n +1)]
        self.d = [0] * (self.n + 1)
        self.f = [[0] * self.m for _ in range(self.n + 1)]

        for u, v in edges:
            self.e[u].append(v)
            self.e[v].append(u)
        
        self.dfs(root, 0)

        for i in range(1, self.m):
            for x in range(1, self.n + 1):
                self.f[x][i] = self.f[self.f[x][i-1]][i-1]
    
    def dfs(self, x, fa):
        self.f[x][0] = fa
        for y in self.e[x]:
            if y == fa:
                continue
            self.d[y] = self.d[x] + 1
            self.dfs(y, x)

    def lca(self, x, y):
        if self.d[x]>self.d[y]:
            x, y = y, x
        
        diff = self.d[y] - self.d[x]
        for i in range(self.m-1, -1, -1):
            if diff & (1 << i):
                y = self.f[y][i]

        if x == y:
            return x
        
        for i in range(self.m-1, -1, -1):
            if self.f[x][i] != self.f[y][i]:
                x = self.f[x][i]
                y = self.f[y][i]
                
        return  self.f[x][0]
    
    def dis(self, x, y):
        return self.d[x] + self.d[y] - self.d[self.lca(x, y)]*2

MOD = 1_000_000_007
N = 100010
p2 = [0]*N
p2[0] = 1
for i in range(1, N):
    p2[i] = p2[i-1]*2 % MOD

class Solution:
    def assignEdgeWeights(self, edges: List[List[int]], queries: List[List[int]]) -> List[int]:
        lca = LCA(edges, 1)
        
        return [( p2[lca.dis(u, v)-1] if u!=v else 0 ) for u, v in queries]
        # graph = defaultdict(list)
        # MOD = 1_000_000_007

        # for u, v, in edges:
        #     graph[u].append(v)
        #     graph[v].append(u)
        
        # @lru_cache
        # def dfs(u, v, p):
        #     ans = float("inf")

        #     for nei in graph[u]:
        #         if nei==v:
        #             return 1
        #         if nei!=p:
        #             ans = min(ans, 1+dfs(nei, v, u))
            
        #     return ans

        # return [(0 if u==v else pow(2, dfs(u, v, u)-1, MOD)) for u, v in queries]
