class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        ob_set = set((x, y) for x, y in obstacles)
        x, y = 0, 0
        dir_x, dir_y = 0, 1
        ans = 0
        for c in commands:
            if c == -2:
                if dir_x>0:
                    dir_x, dir_y = 0, 1
                elif dir_x<0:
                    dir_x, dir_y = 0, -1
                elif dir_y>0:
                    dir_x, dir_y = -1, 0
                elif dir_y<0:
                    dir_x, dir_y = 1, 0
            elif c == -1:
                if dir_x>0:
                    dir_x, dir_y = 0, -1
                elif dir_x<0:
                    dir_x, dir_y = 0, 1
                elif dir_y>0:
                    dir_x, dir_y = 1, 0
                elif dir_y<0:
                    dir_x, dir_y = -1, 0
            else:
                for _ in range(c):
                    nx, ny = x+dir_x, y+dir_y
                    if (nx, ny) in ob_set:
                        break
                    x, y = nx, ny
                    ans = max(ans, x*x+y*y)
        
        return ans
