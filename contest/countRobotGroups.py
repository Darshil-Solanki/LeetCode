class Solution:
    def countGroups(self, position: list[int], speed: list[int], distance: int) -> int:
        n = len(position)
        groups = [speed[0]]
        for i in range(1, n):
            if position[i]-position[i-1]<=distance:
                groups[-1] = speed[i]
            else:
                groups.append(speed[i])
        
        m = len(groups)
        next_group_speed, ans = groups[-1], 1
        for i in range(m-2, -1, -1):
            if groups[i]<=next_group_speed:
                ans += 1
                next_group_speed = groups[i]
        
        return ans
