class Solution:
    def maxArea(self, coords: List[List[int]]) -> int:
        x = defaultdict(list)
        y = defaultdict(list)
        min_y = min_x = float("inf")
        max_y = max_x = float("-inf")
        
        for point_x, point_y in coords:
            min_y, max_y = min(min_y, point_y), max(max_y, point_y)
            min_x, max_x = min(min_x, point_x), max(max_x, point_x)
            x[point_x].append(point_y)
            y[point_y].append(point_x)

        ans = -1
        for point_x, points_y in x.items():
            if len(points_y)>1:
                points_y.sort()
                base = abs(points_y[0]-points_y[-1])
                if min_x!=point_x:
                    ans = max(ans, 0.5*base*abs(point_x-min_x))
                if max_x!=point_x:
                    ans = max(ans, 0.5*base*abs(max_x-point_x))
                    
        for point_y, points_x in y.items():
            if len(points_x)>1:
                points_x.sort()
                base = abs(points_x[-1]-points_x[0])
                if min_y!=point_y:
                    ans = max(ans, 0.5*base*abs(point_y-min_y))
                if max_y!=point_y:
                    ans = max(ans, 0.5*base*abs(max_y-point_y))

        return int(2*ans) if ans>0 else -1
