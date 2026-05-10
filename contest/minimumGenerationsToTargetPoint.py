class Solution:
    def minGenerations(self, points: List[List[int]], target: List[int]) -> int:
        curr_points = defaultdict(bool)
        max_x, max_y, max_z = float("-inf"), float("-inf"), float("-inf")
        def get_key(x, y, z):
            return f"{x}-{y}-{z}"
        for x, y, z in points:
            curr_points[get_key(x, y, z)] = True
            max_x, max_y, max_z = max(max_x, x), max(max_y, y), max(max_z, z)

        tx, ty, tz = target
        target_key = get_key(tx, ty, tz)
        if target_key in curr_points:
            return 0
        if tx>max_x or ty>max_y or tz>max_z:
            return -1
        k = 1
        while True:
            temp = []
            for x1, y1, z1 in points:
                for x2, y2, z2 in points:
                    if x1==x2 and y1==y2 and z1==z2:
                        continue
                    nx, ny, nz = (x1+x2)//2, (y1+y2)//2, (z1+z2)//2
                    new_key = get_key(nx, ny, nz)
                    if new_key == target_key:
                        return k
                    if new_key not in curr_points:
                        curr_points[new_key] = True
                        temp.append([nx, ny, nz])
            
            if not temp:
                return -1
            k += 1
            points.extend(temp)
