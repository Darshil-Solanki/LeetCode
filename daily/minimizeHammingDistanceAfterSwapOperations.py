class UnionSet:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0]*n
    
    def find(self, x):
        if self.parent[x]!=x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return
        if self.rank[x]<self.rank[y]:
            x, y = y, x
        self.parent[y] = x
        if self.rank[x] == self.rank[y]:
            self.rank[x] += 1
        

class Solution:
    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:
        n = len(source)
        uf = UnionSet(n)
        for a, b in allowedSwaps:
            uf.union(a, b)
        
        sets = defaultdict(lambda: defaultdict(int))
        for i, s in enumerate(source):
            f = uf.find(i)
            sets[f][s] += 1

        ans = 0
        for i, t in enumerate(target):
            f = uf.find(i)
            if sets[f][t]>0:
                sets[f][t] -= 1
            else:
                ans += 1
        return ans
