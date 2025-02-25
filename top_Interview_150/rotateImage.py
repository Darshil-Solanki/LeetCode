class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        if n ==1:
            return None
        # Traverse the matrix
        for row in range(n // 2):
            for col in range(row, n - row - 1):
                # Swap the top-left and top-right cells in the current group
                matrix[row][col], matrix[col][n - 1 - row] = (
                    matrix[col][n - 1 - row],matrix[row][col]
                )

                # Swap the top-left and bottom-right cells in the current group
                matrix[row][col], matrix[n - 1 - row][n - 1 - col] = (
                    matrix[n - 1 - row][n - 1 - col],matrix[row][col]
                )

                # Swap the top-left and bottom-left cells in the current group
                matrix[row][col], matrix[n - 1 - col][row] = (
                    matrix[n - 1 - col][row],matrix[row][col]
                )
