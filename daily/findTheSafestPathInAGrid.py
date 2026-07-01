class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        n = len(grid)
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        queue = deque([])
        
        for i in range(n):
            for j in range(n):
                if grid[i][j]:
                    queue.append((i, j))
                    grid[i][j] = 0
                else:
                    grid[i][j] = -1
        
        left, right, ans = 0, 0, -1
        while queue:
            for _ in range(len(queue)):
                i, j = queue.popleft()
                val = grid[i][j]

                for dx, dy in dirs:
                    nx, ny = i+dx, j+dy
                
                    if -1<nx<n and -1<ny<n and grid[nx][ny]==-1:
                        grid[nx][ny] = val + 1
                        right = max(right, val+1)
                        queue.append((nx, ny))

        def check(min_safeness):
            if grid[0][0]<min_safeness or grid[n-1][n-1]<min_safeness:
                return False
            
            queue = deque([(0, 0)])
            seen = [[False]*n for _ in range(n)]
            seen[0][0] = True

            while queue:
                i, j = queue.popleft()
                if i == n-1 and j == n-1:
                    return True
                for dx, dy in dirs:
                    nx, ny = i+dx, j+dy
                    if -1<nx<n and -1<ny<n and not seen[nx][ny] and grid[nx][ny]>=min_safeness:
                        seen[nx][ny] = True
                        queue.append((nx, ny))
            
            return False


        while left<=right:
            mid = (left+right)//2
            if check(mid):
                ans = mid
                left = mid + 1
            else:
                right = mid - 1

        return ans
