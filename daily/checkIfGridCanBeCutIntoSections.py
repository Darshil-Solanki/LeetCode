class Solution:
    def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:
        rectangles.sort(key = lambda x: x[0])
        farthestx = rectangles[0][2]
        vertical_cut = 0
        
        for i in range(1, len(rectangles)):
            sx, ex = rectangles[i][0], rectangles[i][2]
            if sx>=farthestx:
                vertical_cut += 1

            if ex>farthestx: farthestx = ex
            if vertical_cut==2: return True

        rectangles.sort(key = lambda x: x[1])
        farthesty = rectangles[0][3]
        horizontal_cut = 0

        for i in range(1, len(rectangles)):
            sy, ey = rectangles[i][1], rectangles[i][3]
            if sy>=farthesty:
                horizontal_cut += 1
                
            if ey>farthesty: farthesty = ey
            if horizontal_cut==2: return True
            
        return False
