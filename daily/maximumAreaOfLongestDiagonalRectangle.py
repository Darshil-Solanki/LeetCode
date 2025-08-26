class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        area = diagonal = 0

        for l, w in dimensions:
            curr_diagonal = sqrt(l*l + w*w)
            if curr_diagonal>diagonal:
                diagonal = curr_diagonal
                area = l*w
            elif curr_diagonal==diagonal:
                area = max(area, l*w)
        
        return area
