class Solution:
    def nearestDrone(self, drones: list[list[int]], target: list[int]) -> int:
        ans = float("inf")
        min_d = float("inf")
        tx, ty = target
        for i, (x, y, d) in enumerate(drones):
            dist = abs(tx-x)+abs(ty-y)
            if dist<=d and dist<min_d:
                min_d = dist
                ans = i

        return -1 if ans == float("inf") else ans
