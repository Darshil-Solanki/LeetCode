class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: (x[0], -x[1]))
        n = len(points)

        ans = 0
        for i, (x1, y1) in enumerate(points):
            length, height = float("-inf"), y1
            for j in range(i+1, n):
                x2, y2 = points[j]
                if y2<=height and y2>length:
                    ans += 1
                    length = y2
                    if height==y2:
                        height -= 1
        
        return ans
