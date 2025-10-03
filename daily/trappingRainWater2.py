class Cell:
    def __init__(self, height, row, col):
        self.height = height
        self.row = row
        self.col = col

    def __lt__(self, other):
        return self.height<other.height
    

class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        m, n = len(heightMap), len(heightMap[0])

        visited = [[False]*n for _ in range(m)]
        boundary = []

        for i in range(m):
            boundary.append(Cell(heightMap[i][0], i, 0))
            boundary.append(Cell(heightMap[i][n-1], i, n-1))
            visited[i][0] = visited[i][n-1] = True

        for j in range(1, n-1):
            boundary.append(Cell(heightMap[0][j], 0, j))
            boundary.append(Cell(heightMap[m-1][j], m-1, j))
            visited[0][j] = visited[m-1][j] = True

        heapify(boundary)

        tot_water = 0
        while boundary:
            curr_cell = heappop(boundary)
            curr_row, curr_col = curr_cell.row, curr_cell.col
            min_boundary_height = curr_cell.height

            for dr, dc in directions:
                nr, nc = curr_row+dr, curr_col+dc

                if 0<=nr<m and 0<=nc<n and not visited[nr][nc]:
                    nei_height = heightMap[nr][nc]
                    if nei_height < min_boundary_height:
                        tot_water += min_boundary_height-nei_height
                    
                    heappush(boundary, Cell(max(nei_height, min_boundary_height), nr, nc))
                    visited[nr][nc] = True
        
        return tot_water

# same thing using tuple instead of class and if condition instead of for loop more efficient
# class Solution:
#     def trapRainWater(self, heightMap: List[List[int]]) -> int:
#         rows, cols = len(heightMap), len(heightMap[0])
#         heap = []
#         # first and last rows
#         for j in range(cols):
#             heapq.heappush(heap, (heightMap[0][j], 0, j))
#             heightMap[0][j] = -1
#             heapq.heappush(heap, (heightMap[rows-1][j], rows-1, j))
#             heightMap[rows-1][j] = -1
#         # first and last columns
#         for i in range(rows):
#             heapq.heappush(heap, (heightMap[i][0], i, 0))
#             heightMap[i][0] = -1
#             heapq.heappush(heap, (heightMap[i][cols - 1], i, cols-1))
#             heightMap[i][cols-1] = -1
        
#         max_height = heap[0][0]
#         water = 0
#         while heap:
#             cell = heappop(heap)
#             max_height = max(max_height, cell[0])
#             water += max_height - cell[0]
#             i, j = cell[1], cell[2]
#             # left neighbor
#             if i - 1 >= 0 and heightMap[i-1][j] != -1:
#                 heapq.heappush(heap, (heightMap[i-1][j], i-1, j))
#                 heightMap[i-1][j] = -1
#             if i + 1 < rows and heightMap[i+1][j] != -1:
#                 heapq.heappush(heap, (heightMap[i + 1][j], i + 1, j) )
#                 heightMap[i+1][j] = -1
#             if j - 1 >= 0 and heightMap[i][j-1] != -1:
#                 heapq.heappush(heap, (heightMap[i][j-1], i, j-1))
#                 heightMap[i][j-1] = -1
#             if j + 1 < cols and heightMap[i][j+1] != -1:
#                 heapq.heappush(heap, (heightMap[i][j+1], i, j+1))
#                 heightMap[i][j+1] = -1
#         return water
