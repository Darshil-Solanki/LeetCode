class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        m, n = len(moveTime), len(moveTime[0])
        directions = [(0,1), (0, -1), (1, 0), (-1, 0)]
        visited = [ [0]*n for _ in range(m) ]
        heap = [(0, 0, 0)]
        visited[0][0] = 1
        while heap:
            dist, x, y = heappop(heap)
            if x==m-1 and y==n-1: return dist

            for dx, dy in directions:
                cx, cy = x+dx, y+dy
                if -1<cx<m and -1<cy<n and not visited[cx][cy]:
                    heappush(heap, (max(dist, moveTime[cx][cy]) + 1, cx, cy))
                    visited[cx][cy] = 1
            
        return -1
