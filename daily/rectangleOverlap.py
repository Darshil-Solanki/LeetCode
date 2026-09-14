class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        bx1, by1, tx1, ty1 = rec1
        bx2, by2, tx2, ty2 = rec2

        return not(
            tx1 <= bx2 or # left side
            ty1 <= by2 or # bottom side
            bx1 >= tx2 or # right side
            ty2 <= by1 # top side

        )
