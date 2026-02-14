class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        #if poured>5150: return 1
        pyramid = [[0]*k for k in range(1, 102)]
        pyramid[0][0] = poured
        for r in range(query_row+1):
            for c in range(r+1):
                q = (pyramid[r][c]-1)/2
                if q>0:
                    pyramid[r+1][c] += q
                    pyramid[r+1][c+1] += q
        
        return min(1, pyramid[query_row][query_glass])
