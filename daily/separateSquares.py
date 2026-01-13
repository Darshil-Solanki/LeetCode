class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        total_area = 0
        min_y, max_y = float("inf"), float("-inf")
        
        for x, y, l in squares:
            max_y = max(max_y, y+l)
            total_area += l*l

        half_area = total_area/2

        def check(y_line):
            area = 0
            for x, y, l in squares:
                if y<y_line:
                    area += l*min(y_line-y, l)
            return area>=half_area

        left, right = 0, max_y
        while abs(right-left)>1e-5:
            mid = (left+right)/2
            if check(mid):
                right = mid
            else:
                left = mid
        
        return right       
