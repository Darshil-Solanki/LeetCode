class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        wlen = len(word)
        directions = [(-1,0),(1,0),(0,-1),(0,1)]
        def bfs(r, c, i):
            if (not(-1<r<rows and -1<c<cols) or
            board[r][c]!=word[i] or
            (r,c) in seen ):
                return False
            if i==wlen-1:
                return True
            seen.add((r,c))
            flag = False
            for dr, dc in directions:
                cr, cc = r+dr, c+dc
                if (cr,cc) not in seen:
                    flag = flag or bfs(cr, cc, i+1)
            seen.remove((r,c))
            return flag
        seen = set()
        for i in range(rows):
            for j in range(cols):
                if bfs(i, j, 0): return True
        return False

        # Better way 
        # def track(i,j,k):
        #     if(k==wlen):
        #         return True
        #     if(i<0 or i>=rows or j<0 or j>=cols or board[i][j]!=word[k]):
        #         return False
        #     temp=board[i][j]
        #     board[i][j]=None
        #     res = (track(i+1,j,k+1) or track(i-1,j,k+1) or track(i,j+1,k+1) or track(i,j-1,k+1))
        #     board[i][j]=temp
        #     return res           
        # for i in range(rows):
        #     for j in range(cols):
        #         if(board[i][j]==word[0] and track(i,j,0)):
        #             return True
        # return False
