class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        def backtrack(r):
            if r == n:
                ans = ["".join(r) for r in board]
                res.append(ans)
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
        return res
