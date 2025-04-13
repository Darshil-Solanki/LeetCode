class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        xdis, ydis= abs(z-x), abs(z-y)
        if xdis>ydis:
            return 2
        elif xdis<ydis:
            return 1
        else:
            return 0
