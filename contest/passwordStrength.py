class Solution:
    def passwordStrength(self, password: str) -> int:
        point_system = defaultdict(int)
        for c in "abcdefghijklmnopqrstuvwxyz":
            point_system[c] = 1
        for c in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            point_system[c] = 2
        for c in "0123456789":
            point_system[c] = 3
        for c in "!@#$":
            point_system[c] = 5

        points = 0
        for c in password:
            if point_system[c]:
                points += point_system[c]
                point_system[c] = 0
        return points
