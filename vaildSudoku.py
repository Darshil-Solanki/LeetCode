class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = tuple(set() for i in range(9))
        cols = tuple(set() for i in range(9))
        square = tuple(set() for i in range(9))
        for i in range(9):
            for j in range(9):
                curr = board[i][j]
                if curr==".":
                    continue
                s = self.whichSquare(i,j)
                if curr in rows[i] or curr in cols[j] or curr in square[s]:
                    return False
                rows[i].add(curr)
                cols[j].add(curr)
                square[s].add(curr)
        return True
    def whichSquare(self, i,j):
        if i<3 and j<3:
            return 0
        elif i<6 and j<3:
            return 1
        elif i<9 and j<3:
            return 2
        elif i<3 and j<6:
            return 3
        elif i<6 and j<6:
            return 4
        elif i<9 and j<6:
            return 5
        elif i<3 and j<9:
            return 6
        elif i<6 and j<9:
            return 7
        elif i<9 and j<9:
            return 8
