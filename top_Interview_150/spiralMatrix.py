class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        endM, endN = len(matrix), len(matrix[0])
        if endM==1:
            return matrix[0]
        if endN == 1:
            return [i[0] for i in matrix]
        result = []
        i,j = 0, 0
        loop = endN//2+1 if endN%2 else endN//2
        for iteration in range(loop):
            #first row
            while i<endM and j<endN:
                result.append(matrix[i][j])
                j+=1
            j-=1
            i+=1
            #last column
            while i<endM and j<endN:
                result.append(matrix[i][j])
                i+=1
            i-=1
            j-=1
            #last row
            while j>=iteration and i>iteration:
                result.append(matrix[i][j])
                j-=1
            j+=1
            i-=1
            #first column
            while i>iteration and j<endN-1:
                result.append(matrix[i][j])
                i-=1
            i+=1
            j+=1
            endM-=1
            endN-=1
        return result

    # Better way of doing this with direction and total count
    # def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
    #     m, n = len(matrix), len(matrix[0])
    #     count, direction = m * n, 1
    #     i, j, result = 0, -1, []

    #     while len(result) != count:
    #         for _ in range(n):
    #             j += direction
    #             result.append(matrix[i][j])
    #         m -= 1

    #         for _ in range(m):
    #             i += direction
    #             result.append(matrix[i][j])
    #         n -= 1

    #         direction *= -1
        
    #     return result
