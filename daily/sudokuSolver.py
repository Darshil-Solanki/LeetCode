class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        row = [set() for _ in range(9)]
        col = [set() for _ in range(9)]
        box = [set() for _ in range(9)]

        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    row[i].add(board[i][j])
                    col[j].add(board[i][j])
                    box[(i//3)*3 + (j//3)].add(board[i][j])

        def solve(r, c):

            if r >= 9:
                return True
            
            if c >= 9:
                return solve(r+1, 0)
            
            if board[r][c] != '.':
                return solve(r, c+1)
            
            for i in range(1, 10):

                char = str(i)
                if char not in row[r] and char not in col[c] and char not in box[(r//3)*3 + c//3]:
                    board[r][c] = char
                    row[r].add(char)
                    col[c].add(char)
                    box[(r//3)*3+(c//3)].add(char)
                    if solve(r, c+1):
                        return True
                    board[r][c] = '.'
                    row[r].remove(char)
                    col[c].remove(char)
                    box[(r//3)*3+(c//3)].remove(char)
            
            return False

        solve(0, 0)
