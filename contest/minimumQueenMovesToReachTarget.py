class Solution:
    def minQueenMoves(self, source: list[int], target: list[int]) -> int:
        def reach_in_move():
            if source[0] == target[0] or source[1] == target[1]:
                return True
            
            for dx, dy in [(-1,-1), (-1,1), (1,-1), (1,1)]:
                cx, cy = source
                while 0<cx+dx<9 and 0<cy+dy<9:
                    cx += dx
                    cy += dy
                    if [cx, cy] == target:
                        return True
            return False
            
        if source == target:
            return 0
        if reach_in_move():
            return 1
        return 2
