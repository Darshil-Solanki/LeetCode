class Solution:
    def minBishopMoves(self, source: list[int], target: list[int]) -> int:
        color = sum(source)
        if color%2:#black odd
            if not sum(target)%2:
                return -1
        else:
            if sum(target)%2:
                return -1

        # if reachable directly
        for dx, dy in [(-1, -1), (-1, 1), (1, -1), (1, 1)]:
            cx, cy = source
            while 0<cx<9 and 0<cy<9:
                if [cx, cy] == target:
                    return 1
                cx += dx
                cy += dy
            
        return 2
