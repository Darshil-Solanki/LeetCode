class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x:x[1])
        l=count=1
        shoted = points[0][1]
        while l<len(points):
            if points[l][0]>shoted:
                count+=1
                shoted = points[l][1]
            l+=1
        return count
with open("user.out", "w") as f:
    for points in map(loads, stdin):
        s = Solution()
        f.write(f"{s.findMinArrowShots(points)}\n")
exit(0)
