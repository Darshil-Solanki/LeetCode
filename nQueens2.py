class Solution:
    def totalNQueens(self, n: int) -> int:
        self.ans = 0
        def backtrack(r):
            if r == n:
                self.ans += 1
                return
            for c in range(n):
                if c in placeCol or r+c in placeDiagPos or r-c in placeDiagNeg:
                    continue
                board[r][c]="Q"
                placeCol.add(c)
                placeDiagPos.add(r+c)
                placeDiagNeg.add(r-c)

                backtrack(r+1)

                board[r][c]="."
                placeCol.remove(c)
                placeDiagPos.remove(r+c)
                placeDiagNeg.remove(r-c)


        board = [ ["."]*n for _ in range(n) ]
        placeCol, placeDiagPos, placeDiagNeg = set(), set(), set()
        backtrack(0)
        return self.ans
