class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        nSquare = n*n

        def get_position(num):
            r = (num-1)//n
            c = (num-1)%n
            if r%2==0:
                return board[n-1-r][c]
            else:
                return board[n-1-r][n-1-c]

        queue, seen = [1], {1}
        pathCount = 0
        while queue:
            pathCount+=1
            curr_len = len(queue)
            for _ in range(curr_len):
                node = queue.pop(0)
                for roll in range(1,7):
                    nextSquare = node + roll
                    if nextSquare>nSquare:
                        continue
                    destination = get_position(nextSquare)      #Better way could be iterate over each position and create hash map for only snacks and ladder and get destination from it.
                    if destination!=-1:
                        nextSquare = destination
                    if nextSquare == nSquare:
                        return pathCount
                    if nextSquare not in seen:
                        seen.add(nextSquare)
                        queue.append(nextSquare)
                
        return -1
