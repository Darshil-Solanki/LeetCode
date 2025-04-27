class Solution:
    def countCoveredBuildings(self, n: int, buildings: List[List[int]]) -> int:
        if len(buildings)<5: return 0
        buildings.sort()
        all_y_at_x = defaultdict(list)
        all_x_at_y = defaultdict(list)

        for x, y in buildings:
            all_y_at_x[x].append(y)
            all_x_at_y[y].append(x)


        ans = 0
        for i in range(1, len(buildings)-1):
            x, y = buildings[i]
            horizontal_surrounded = vertical_surrounded = False
            # up and down
            if len(all_x_at_y[y])>1 and all_x_at_y[y][0]<x and all_x_at_y[y][-1]>x:
                vertical_surrounded = True
            # left and right
            if len(all_y_at_x[x])>1 and all_y_at_x[x][0]<y and all_y_at_x[x][-1]>y:
                horizontal_surrounded = True

            if horizontal_surrounded and vertical_surrounded:
                ans += 1

        return ans
