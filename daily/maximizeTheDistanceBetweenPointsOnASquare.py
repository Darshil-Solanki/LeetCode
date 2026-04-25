class Solution:
    def maxDistance(self, side: int, points: List[List[int]], k: int) -> int:
        dist_origin = []
        perimeter = side * 4

        for x, y in points:
            if x==0:
                dist_origin.append(y)
            elif y==side:
                dist_origin.append(y+x)
            elif x==side:
                dist_origin.append(side*3 - y)
            else:
                dist_origin.append(perimeter - x)
        
        dist_origin.sort()

        def check(limit):
            for start in dist_origin:
                end = start + perimeter - limit
                cur = start
                for _ in range(k-1):
                    idx = bisect_left(dist_origin, cur+limit)
                    if idx == len(dist_origin) or dist_origin[idx]>end:
                        cur = -1
                        break
                    cur = dist_origin[idx]
                if cur>=0:
                    return True
            return False

        ans = 0
        left, right = 1, side
        while left<=right:
            mid = (left+right)//2
            if check(mid):
                left = mid + 1
                ans = mid
            else:
                right = mid -1
        
        return ans
