# Copied from solutions
class DSU:
    def __init__(self, parent):
        self.parent = parent
    
    def find(self, x):
        if self.parent[x] == x:
            return x
        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def join(self, x, y):
        self.parent[self.find(x)] = self.find(y)
    
MAX_STABILITY = 2_00_000

class Solution:
    def maxStability(self, n: int, edges: List[List[int]], k: int) -> int:
        ans = -1
        if len(edges)<n-1:
            return -1
        
        must_edges = [e for e in edges if e[3]]
        optional_edges = [e for e in edges if not e[3]]
        if len(must_edges)>n-1:
            return -1
        optional_edges.sort(key = lambda x: x[2], reverse=True)

        selected_init = 0
        must_min_stability = MAX_STABILITY
        dsu_init = DSU(list(range(n)))

        for u, v, s, must in must_edges:
            if dsu_init.find(u) == dsu_init.find(v) or selected_init == n-1:
                return -1
            dsu_init.join(u, v)
            selected_init += 1
            must_min_stability = min(must_min_stability, s)
        
        l = 0
        r = must_min_stability

        while l<r:
            mid = l + ((r - l + 1) >> 1)
            dsu = DSU(dsu_init.parent[:])
            selected = selected_init
            doubled_count = 0
            for u, v, s, must in optional_edges:
                if dsu.find(u) == dsu.find(v):
                    continue
                if s>=mid:
                    dsu.join(u, v)
                    selected += 1
                elif doubled_count < k and s*2>=mid:
                    doubled_count += 1
                    dsu.join(u, v)
                    selected += 1
                else:
                    break
                if selected == n-1:
                    break
            if selected != n-1:
                r = mid -1
            else:
                ans = l = mid
        return ans
