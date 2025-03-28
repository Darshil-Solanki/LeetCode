class Solution:
    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        m, n = len(grid), len(grid[0])
        query_dict = defaultdict(list)
        for i, q in enumerate(queries):
            query_dict[q].append(i)
        

        query = sorted(query_dict.keys())
        results = [0]*len(queries)
        heap = [(grid[0][0], 0, 0)]
        visited = [[False]*n for _ in range(m)]
        visited[0][0] = True
        points = 0

        for q in query:
            while heap and heap[0][0]<q:
                _, i, j = heappop(heap)
                points+=1
                if i-1>-1 and not visited[i-1][j]:
                    heappush(heap, (grid[i-1][j], i-1, j))
                    visited[i-1][j] = True
                if i+1<m and not visited[i+1][j]:
                    heappush(heap, (grid[i+1][j], i+1, j))
                    visited[i+1][j] = True
                if j-1>-1 and not visited[i][j-1]:
                    heappush(heap, (grid[i][j-1], i, j-1))
                    visited[i][j-1] = True
                if j+1<n and not visited[i][j+1]:
                    heappush(heap, (grid[i][j+1], i, j+1))
                    visited[i][j+1] = True


            for idx in query_dict[q]:
                results[idx]=points
        
        return results
