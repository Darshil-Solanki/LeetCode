class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        seen = set()
        def dfs(r,c):
            seen.add((r,c))
            queue = [(r,c)]
            while queue:
                cr, cc = queue.pop(0)
                direction = [ [0, -1], [0, 1], [-1, 0], [1, 0] ]
                for dr, dc in direction:
                    r, c = cr+dr, cc+dc
                    if ( -1<r<rows and -1<c<cols and
                        board[r][c]=="O" and
                        (r,c) not in seen):
                        seen.add((r,c))
                        queue.append((r,c))

        rows, cols = len(board), len(board[0])
        for r in range(0,rows,rows-1 if rows!= 1 else 1):
            for c in range(cols):
                if board[r][c]=="O":
                    dfs(r,c)
        for r in range(rows):
            for c in range(0, cols, cols-1 if cols!= 1 else 1):
                if board[r][c]=="O":
                    dfs(r,c)
        for r in range(1,rows):
            for c in range(1,cols):
                if board[r][c]=="O" and (r, c) not in seen:
                    board[r][c]="X"

        # DFS way
        # rows , cols = len(board),len(board[0])
        # visit = set()
        # direction = [[1,0],[-1,0],[0,1],[0,-1]]
        # def dfs(r,c):
        #     if r<0 or c<0 or r==rows or c==cols or board[r][c]!='O':
        #         return
        #     board[r][c]='T'
        #     dfs(r,c+1)
        #     dfs(r,c-1)
        #     dfs(r+1,c)
        #     dfs(r-1,c)

        # for r in range(0,rows,rows-1 if rows!= 1 else 1):
        #     for c in range(cols):
        #         if board[r][c]=="O":
        #             dfs(r,c)
        # for r in range(rows):
        #     for c in range(0, cols, cols-1 if cols!= 1 else 1):
        #         if board[r][c]=="O":
        #             dfs(r,c)

        # for i in range(rows):
        #     for j in range(cols):
        #         if board[i][j]=='O':
        #             board[i][j] = 'X'
        #         elif board[i][j]=='T':
        #             board[i][j] = 'O'
