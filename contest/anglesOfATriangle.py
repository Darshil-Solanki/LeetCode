class Solution:
    def internalAngles(self, sides: list[int]) -> list[float]:
        a, b, c = sorted(sides)
        if all((a+b>c, b+c>a, c+a>b)):
            angle1 = degrees(acos((b*b + c*c - a*a)/(2*b*c)))
            angle2 = degrees(acos((a*a + c*c - b*b)/(2*a*c)))
            angle3 = 180 - angle1 - angle2
            return sorted([angle1, angle2, angle3])
        return []
