class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m, n = len(heights), len(heights[0])
        visited = [[0]*n for _ in range(m)]
        queue = deque([])
        ans = []
        def  is_visited(i, j, from_ocean):
            return (visited[i][j] & from_ocean) != 0
        
        def add(i, j, from_ocean):
            if (visited[i][j]  & from_ocean)==0:
                visited[i][j] |= from_ocean
                queue.append((i, j, from_ocean))

        for i in range(n): add(0, i, 1)
        for i in range(m): add(i, 0, 1)
        for i in range(m): add(i, n-1, 2)
        for i in range(n): add(m-1, i, 2)

        while queue:
            i, j, ocean = queue.popleft()
            curr_h = heights[i][j]
            if j+1<n and not is_visited(i, j+1, ocean) and curr_h<=heights[i][j+1]:
                visited[i][j+1] |= ocean
                queue.append((i, j+1, ocean))
            if j-1>-1 and not is_visited(i, j-1, ocean) and curr_h<=heights[i][j-1]:
                visited[i][j-1] |= ocean
                queue.append((i, j-1, ocean))
            if i+1<m and not is_visited(i+1, j, ocean) and curr_h<=heights[i+1][j]:
                visited[i+1][j] |= ocean
                queue.append((i+1, j, ocean))
            if i-1>-1 and not is_visited(i-1, j, ocean) and curr_h<=heights[i-1][j]:
                visited[i-1][j] |= ocean
                queue.append((i-1, j, ocean))
        
        for i in range(m):
            for j in range(n):
                if visited[i][j]==3:
                    ans.append([i, j])
        return ans
