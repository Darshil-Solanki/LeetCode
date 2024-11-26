class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])
        tBoard = [row[:] for row in board]
        for i in range(m):
            for j in range(n):
                liveNeighbour = 0
                if i-1>-1:
                    if j-1>-1:
                        if tBoard[i-1][j-1]:
                            liveNeighbour+=1
                    if j+1<n:
                        if tBoard[i-1][j+1]:
                            liveNeighbour+=1
                    if tBoard[i-1][j]:
                        liveNeighbour+=1
                if j-1>-1:
                    if tBoard[i][j-1]:
                        liveNeighbour+=1
                if j+1<n:
                    if tBoard[i][j+1]:
                        liveNeighbour+=1
                if i+1<m:
                    if j-1>-1: 
                        if tBoard[i+1][j-1]:
                            liveNeighbour+=1
                    if tBoard[i+1][j]:
                        liveNeighbour+=1
                    if j+1<n:
                        if tBoard[i+1][j+1]:
                            liveNeighbour+=1
                if not tBoard[i][j]:
                    board[i][j] = 1 if liveNeighbour==3 else 0
                else:
                    board[i][j] = 1 if 1<liveNeighbour<4 else 0
    # Better and Proper solution without use extra memory of board
    # def gameOfLife(self, board: List[List[int]]) -> None:
    #     """
    #     Do not return anything, modify board in-place instead.
    #     """
    #     m, n = len(board), len(board[0])
        
    #     # Direction vectors for the 8 possible neighbors
    #     directions = [(-1, -1), (-1, 0), (-1, 1),
    #                   (0, -1),         (0, 1),
    #                   (1, -1), (1, 0), (1, 1)]
        
    #     # First pass: Encode the next state
    #     for i in range(m):
    #         for j in range(n):
    #             liveNeighbours = 0
    #             for d in directions:
    #                 ni, nj = i + d[0], j + d[1]
    #                 if 0 <= ni < m and 0 <= nj < n:
    #                     if board[ni][nj] == 1 or board[ni][nj] == 3:
    #                         liveNeighbours += 1
                
    #             # Determine the next state based on the current state and the number of live neighbors
    #             if board[i][j] == 1:
    #                 # Currently alive
    #                 if liveNeighbours < 2 or liveNeighbours > 3:
    #                     board[i][j] = 3  # Will die
    #                 else:
    #                     board[i][j] = 1  # Remains alive
    #             else:
    #                 # Currently dead
    #                 if liveNeighbours == 3:
    #                     board[i][j] = 2  # Will become alive
    #                 else:
    #                     board[i][j] = 0  # Remains dead

    #     # Second pass: Decode the next state
    #     for i in range(m):
    #         for j in range(n):
    #             if board[i][j] == 1 or board[i][j] == 2:
    #                 board[i][j] = 1  # Alive
    #             else:
    #                 board[i][j] = 0  # Dead
