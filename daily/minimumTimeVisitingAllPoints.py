class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        px, py = points[0]

        ans = 0
        for i in range(1, len(points)):
            cx, cy = points[i]
            ans += max(abs(cx-px), abs(cy-py))
            px, py = cx, cy
        
        return ans
