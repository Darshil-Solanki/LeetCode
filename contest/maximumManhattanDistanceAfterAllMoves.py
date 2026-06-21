class Solution:
    def maxDistance(self, moves: str) -> int:
        x, y = 0, 0
        extra = 0
        for d in moves:
            if d == "U":
                y += 1
            elif d == "D":
                y -= 1
            elif d == "L":
                x -= 1
            elif d == "R":
                x += 1
            else:
                extra += 1
        return abs(x)+abs(y)+extra
