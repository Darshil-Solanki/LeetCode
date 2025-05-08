class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        m, n = len(moveTime[0]), len(moveTime)
        heap = [(0, 0, 0, 0)]
        visited = set([(0,0)])
        while heap:
            dis, u, v, move = heappop(heap)
            if (u, v) == (n-1, m-1): return dis

            for dx, dy in [(0, 1),(0, -1), (1,0), (-1, 0)]:
                nu, nv = u+dx, v+dy
                if -1<nu<n and -1<nv<m and (nu, nv) not in visited:
                    visited.add((nu, nv))
                    new_dist = max(dis, moveTime[nu][nv]) + move%2 + 1
                    heappush(heap, (new_dist, nu, nv, move+1))
