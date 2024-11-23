class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        globalPoints = 0
        for i in range(len(points)):
            hashMap = defaultdict(int)
            x1, y1 = points[i][0], points[i][1]
            maxPoints = 0
            for j in range(i+1, len(points)):
                x2, y2 = points[j][0], points[j][1]
                x, y = x2-x1, y2-y1
                gcdVal = gcd(x, y)
                x//=gcdVal; y//=gcdVal
                if x != 0 and y != 0 and ((y < 0 and x > 0) or (x < 0 and y < 0)):
                    x, y = -x, -y
                if y == 0:  # Handle horizontal line
                    key = "horizontal"
                elif x == 0:  # Handle vertical line
                    key = "vertical"
                else:
                    key = f"{x}/{y}"

                hashMap[key]+=1
                if hashMap[key]>maxPoints:
                    maxPoints = hashMap[key]
            globalPoints = max(globalPoints, maxPoints+1)
        return globalPoints
